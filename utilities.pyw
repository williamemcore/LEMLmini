
import datetime
import inspect
import os
import re
import sys
import time
import zipfile
import serial
import threading
import queue
import socket
import json
import time
import binascii
import glob
from collections import OrderedDict
from decimal import *

# Emcore specific
from constants import *





def MySleep( sleeptime:float ):
    """Sleep and prevent Control-C interrupt

    sleeptime: in second

    return: none
    """
    log.debug( 'Enter {0} sec'.format( sleeptime ) )

    try:
        time.sleep( sleeptime )
    except:
        pass

    log.debug( 'Exit' )
    return



def SocketWrite( addr:tuple, command:str ) -> bool:
    """Wrapper for socket write command
    Supports AF_INET address family.

    addr: a tuple of the ip address and port.
              ip address should be a string representing the hostname in
              internet notation or IPV4 address.
              port is an integer
          i.e. ( '10.1.1.1', 2345 )
    command: command to send through socket

    Return: True if success
            False if failed
    """
    log.debug( 'Enter gateway addr "{}", command "{}"'.format( addr, command ) )

    try:
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        s.bind( addr )
        s.listen( 5 )
        # Set the wait time for accept to 3 seconds
        s.settimeout( 3 )
        client, addr = s.accept()
        sendmsg = binascii.a2b_hex( command )
        client.send( sendmsg )
        data = client.recv( 1024 )
        if not data:
            log.debug( 'No data' )
            client.close()
        log.debug( 'data: {}, equip addr: {}'.format( data, addr ) )
        client.close()
        log.debug( 'close client' )

    except Exception as e:
        log.debug( e )

    s.close()

    log.debug( 'Exit' )
    return True



def GpibWrite( res_inst, command:str ) -> bool :
    """Wrapper for PyVISA write command with error checking

    Return: True if write succeeded
            False if write failed
    """
    log.debug( 'Enter command "{0}"'.format( command ) )

    try:
        response = res_inst.write( command )
    except:
        log.debug( 'write "{0}" failed!'.format( command ) )
        return False

    if ( response[ 1 ] != 0 ):
        log.debug( '"{0}" failed! "{1}"'.format(
            command, response[ 1 ] ) )
        return False

    log.debug( 'Exit' )
    return True



def LinearFit( partialData: OrderedDict(), loFreq: Decimal,
              hiFreq: Decimal ) -> float:
    """ Use Linear Fit algorithm to calculate the slope of the line.

    partialData: ordered dictionary of Frequencies as keys and Amplitudes
            as values
    loFreq: the start frequency in the board parameters
    hiFreq: the stop frequency in the board parameters

    Returns: the slope of the trendline for the response
    """
    log.debug( 'Enter' )

    Sx = 0
    Sy = 0
    Sxy = 0
    Sxx = 0
    points = 1

    for freq, amp in partialData.items():
        Sx += freq
        Sy += amp
        Sxy += freq * amp
        Sxx += freq ** 2
        points += 1

    slope = (Sxy - Sx * Sy / points ) / ( Sxx - Sx ** 2 / points )

    log.debug( 'Exit {0}'.format( slope ) )
    return slope



def read_json_file( filename:str ) -> OrderedDict:
    '''Read a JSON file type and return it as python dictionary

    file: Json file

    Return:
        rValue - Python dictionary of the file content
    '''
    log.debug( 'Enter Parameter: {0}'.format( filename ) )

    rValue = None
    try:
        with open( filename, 'r' ) as fhandle:
            rValue = json.load( fhandle, object_pairs_hook = OrderedDict )
    except Exception as e:
        log.error( 'Failed to read Json file {0}. Error {1}'.format( filename, e ) )
    # end try

    log.debug( 'Exit' )
    return rValue
# end function



def write_json_file( filename:str, InfoDict:dict ) -> bool:
    '''Write a JSON file type from an OrderedDict or python dictionary

    filename: Filename with json file extension
    InfoDict: OrderedDict or python dictionary to be written as json file type

    Return:
        rValue - Python dictionary of the file content
    '''
    log.debug( 'Enter Parameter: {0}'.format( filename ) )

    indent = 4
    fhPerm = 'w+'

    try:
        with open( filename, fhPerm ) as fh:
            json.dump( InfoDict, fh, indent = indent )
        # end with
    except Exception as e:
        log.error( 'Failed to write to Json file. Exception '
                   'encountered {0}'.format( e ) )
        return False
    # end if

    log.debug( 'Exit' )
    return True
# end function





class logs( object ):

    # Class attribute ( Global )
    clientAddress     = () # Tuple
    Streamer_loglevel = [] # List

    log_message_queue = queue.Queue( maxsize = 0 ) # Queue
    log_thread_semaphore = threading.Semaphore( value = 0 ) # Semaphore
    log_thread = None # Thread

    log_thread_started_event = threading.Event()
    log_thread_ended_event = threading.Event()
    event_wait_time = 10

    osPathSep     = os.path.sep
    scriptName    = sys.argv[ 0 ]
    scriptDirName = os.path.dirname( scriptName )
    scriptAbsPath = os.path.abspath( scriptDirName )

    debug_filename = scriptAbsPath + osPathSep + LOG_DEBUG_FILENAME
    info_filename  = scriptAbsPath + osPathSep + LOG_INFO_FILENAME
    error_filename = scriptAbsPath + osPathSep + LOG_ERROR_FILENAME
    fail_filename  = scriptAbsPath + osPathSep + LOG_FAIL_FILENAME

    output_screen_flag = True
    output_debug_flag  = True
    output_info_flag   = True
    output_error_flag  = True
    output_fail_flag   = True



    def __init__( self ):
        ''' Constructor function initializes all variables used throughout the
        class
        '''
        self.logger_name = ''
        self.func_name   = ''
        self.class_name  = ''
    # end __init__



    def initialize( self,
                    loglevel = 5,
                    keepOldLogs = True,
                    keepOldAgeMaxDays = 15,
                    createNewLogs = True ) -> bool:
        """ Initialize logs thread. Attempts to store the previous log files
            to an archive directory. Starts the log thread
        Input   : None
        Return  : True: logs files are initialized
                  False: logs files are Failed to initialized
        """
        rValue = True

        # How much logging
        if ( type( loglevel ) == type( 1 ) and loglevel >= 0 ):
            self.processLoglevel( loglevel = loglevel )
        # end if

        if keepOldLogs:
            if not self.manage_old_logfiles( scriptAbsPath = logs.scriptAbsPath,
                                           logMaxAge = keepOldAgeMaxDays ):
                print( 'Failed in storing older files in archive directory' )
            # end if
        # end if

        if createNewLogs:
            if not self.create_log_files():
                print( 'Failed creating new log files' )
                if ( type( loglevel ) == type( 1 ) and loglevel == 0 ):
                    print( 'Log level is set to not require logging to files.' +
                           ' Creating new files failed although bypassed' )
                else:
                    print( 'Return value will be false' )
                    rValue = False
                # end if
            # end if
        # end if

        # Start log thread
        logs.log_thread = threading.Thread( target = logs.log_thread_work,
                                            daemon = True ) # Thread
        logs.log_thread.start()

        # Event returns true if the flag has been set by thread starting
        #   returns false if timeout is hit
        if logs.log_thread_started_event.wait( timeout = logs.event_wait_time ):
            if not logs.is_log_thread_alive():
                print( 'Failed to start log thread, even though start event' +
                       'was set to true' )
                rValue = False
            # end if
        else:
            print( 'Failed to start log thread, start event ' +
                   'flag wait timeoutof {int1} ' +
                   'expired'.format( int1 = logs.event_wait_time  ) )
            rValue = False
        # end if

        return rValue
    # end function



    def is_log_thread_alive():
        if logs.log_thread.is_alive():
            return True
        else:
            return False
        # end if
    # end function



    def log_thread_work():
        ''' Life of the log thread. Wait for log message to be placed in
            queue and semaphore or finish signal
        '''
        # Let initializing function know we have started
        logs.log_thread_started_event.set()

        while True:
            with logs.log_thread_semaphore:
                filename_message = logs.log_message_queue.get()
                if filename_message:
                    logs._write2file( filename_message = filename_message)
                else:
                    break
            # end with log_thread_semaphore
        # end while

        logs.log_thread_ended_event.set()
        print( '"logs" thread exiting' )
    # end function



    def log_thread_kill( timeout = 60 ):
        logs.log_message_queue.put( False )
        logs.log_thread_semaphore.release()

        logs.log_thread_ended_event.wait( timeout = timeout )

        # Zip up files
        ziplogfiles()
    # end function



    def _write2file( filename_message:dict ):
        try:
            with open( filename_message[ LOG_FILENAME ], 'a' ) as fh:
                #fh.write( filename_message[ LOG_MESSAGE ] + os.linesep )
                fh.write( filename_message[ LOG_MESSAGE ] + '\n' )
            # end with
        except Exception as e:
            print( str.format( 'Error: Log Error or I/O error {excp1}',
                   excp1 = e ) )
        # end try
    # end function



    def screenOutput( self, message ):
        if logs.output_screen_flag:
            print( message )
        # end if
    # end function



    def manage_old_logfiles( self, scriptAbsPath:str, logMaxAge:int ):
        rValue = True
        osPathSep = os.path.sep
        archivePath = scriptAbsPath + osPathSep + 'Archive'
        testinfofn = ''


        # What to do with old log files, if any
        #   Check if archive folder exist
        if not os.path.exists( archivePath ):
            os.makedirs( archivePath )
        # end if

        # Check if archive folder exist one more time
        if not os.path.exists( archivePath ):
            print ( 'Did not find "Archive" folder as expected. Cannot ' +
                    'store previous log files, if any' )
        else:
            # Updating Archive folder
            old_log_files =  os.listdir( archivePath )

            print( "Deleting old file please wait ..." )
            for old_file in old_log_files:
                old_file_path = archivePath + osPathSep + old_file
                try:
                    # Getting file info
                    file_Stat = FileStat( old_file_path )
                    file_Stat.stat()
                except:
                    print( 'log.Initialize: error: Failed to get file info: ' +
                            old_file )
                    rValue = False

                # Delete log file its older than log_age from archive folder
                if ( file_Stat.age_in_days() >= logMaxAge ):
                    os.remove( old_file_path )
            # end for
        # end if

        return rValue
    # end function



    def create_log_files( self ):
        rValue = True

        log_file_list = ( logs.info_filename,  logs.debug_filename,
                          logs.error_filename, logs.fail_filename )

        for new_file in log_file_list:
            try:
                open( new_file, 'w' ).close()
            except:
                print( 'Failed to clean/create log file ' +
                       '{str1}'.format( str1 = new_file ) )
                rValue = False
        # end for

        return rValue
    # end function



    def get_last_testinfo_file( self ) -> str:
        ''' Want to store the test result file in the zip file which we used
            to only store the log files in.

        Return:
            latestfn: filename of the latest testinfo file
            None: Testinfo not found
        '''
        latestsize = float( 0 ) # Want the larger file
        latesttime = float( 0 ) # Want the latest testinfo
        latestfn = ''
        retlist = []

        retlist1 = glob.glob( '*_supertestresult.json' )
        retlist2 = glob.glob( 'testinfo_*.json' )
        retlist = retlist1 + retlist2

        if ( len( retlist ) == 0 ):
            return None
        # end if

        for i in range( 0, len( retlist ) ):
            tempfnstat =  os.stat( retlist[ i ] )
            currtime = tempfnstat.st_mtime
            currsize = tempfnstat.st_size
            if ( currtime < latesttime ):
                continue
            elif ( currtime == latesttime ):
                if ( currsize <= latestsize ):
                    continue
                # end if
            # end if

            latestfn = retlist[ i ]
            latesttime = currtime
            latestsize = currsize
        # end for

        # Logs not initialized at this point
        print( 'Found latest testinfo file {0} with time {1}'.format( latestfn,
            datetime.datetime.fromtimestamp( latesttime ) ) )

        return latestfn
    # end function



    def debug( self, message ):
        """
        Purpose : Write message on debug.log
        Input   : message to write ,logger name
        Return  : None
        """
        if "debug" in logs.Streamer_loglevel:
            self.streamer( message )
        # end if

        self.__updateInfo()

        if logs.output_debug_flag:
            timestamp = datetime.datetime.now().strftime( LOG_DATE_FORMATTING )

            # String format is specific to DEBUG file
            # Adding timestamp, log object initializing location,
            #   calling function class name (if any), calling function
            # Python "String Formatting Operations"
            # - : The converted value is left adjusted (overrides the '0'
            #       conversion if both are given).
            # s : Converts any Python object using str
            msg2w = '%-18s %-18s %s%s %s ' % ( timestamp,
                                               self.logger_name,
                                               self.class_name,
                                               self.func_name,
                                               message )

            logs.log_message_queue.put( { "filename": logs.debug_filename,
                                          "message" : msg2w } )
            logs.log_thread_semaphore.release()
        # end if

        # Output to screen
        self.screenOutput( '{str1}{str2} {str3}'.format( str1 = self.class_name,
                                                         str2 = self.func_name,
                                                         str3 = message ) )
    # end function debug



    def info( self, message ):
        """
        Purpose : Write on console and append message on info.log
        Input   : message to write ,Logger Name
        Return  : None
        """
        if "info" in logs.Streamer_loglevel:
            self.streamer(message)
        # end if

        if logs.output_info_flag:
            timestamp = datetime.datetime.now().strftime( LOG_DATE_FORMATTING )

            # String format is used by Info, Error, Fail functions
            # Python "String Formatting Operations"
            # - : The converted value is left adjusted (overrides the '0'
            #       conversion if both are given).
            # s : Converts any Python object using str
            msg2w = '%-18s %-18s %5s ' % ( timestamp, self.logger_name, message )

            logs.log_message_queue.put( { "filename": logs.info_filename,
                                          "message" : msg2w } )
            logs.log_thread_semaphore.release()
        # end if

        # Output to debug file
        self.debug( message )

    # end function info



    def error( self, message ):
        """
        Purpose : Write on console and append message on error.log
        Input   : message to write , logger name
        Return  : None
        """
        # Add error string prefix
        message =  'Error: {str1}'.format( str1 = message )

        if "error" in logs.Streamer_loglevel:
            self.streamer( message )
        # end if

        if logs.output_error_flag:
            timestamp = datetime.datetime.now().strftime( LOG_DATE_FORMATTING )

            # String format is used by Info, Error, Fail functions
            # Python "String Formatting Operations"
            # - : The converted value is left adjusted (overrides the '0'
            #       conversion if both are given).
            # s : Converts any Python object using str
            msg2w = '%-18s %-18s %5s ' % ( timestamp, self.logger_name, message )

            logs.log_message_queue.put( { "filename": logs.error_filename,
                                          "message" : msg2w } )
            logs.log_thread_semaphore.release()
        # end if

        # Output to info file
        self.info( message )

    # end function error



    def fail( self, message ):
        """
        Purpose : Write on console and append message on fail.log
        Input   : message to write , logger name
        Return  : None
        """
        # Add fail string prefix
        message =  'Fail: {str1}'.format( str1 = message )

        if "fail" in logs.Streamer_loglevel:
            self.streamer( message )
        # end if

        if logs.output_fail_flag:
            timestamp = datetime.datetime.now().strftime( LOG_DATE_FORMATTING )

            # String format is used by Info, Error, Fail functions
            # Python "String Formatting Operations"
            # - : The converted value is left adjusted (overrides the '0'
            #       conversion if both are given).
            # s : Converts any Python object using str
            msg2w = '%-18s %-18s %5s ' % ( timestamp, self.logger_name, message )

            logs.log_message_queue.put( { "filename": logs.fail_filename,
                                          "message" : msg2w } )
            logs.log_thread_semaphore.release()
        # end if

        # Output to info file
        self.info( message )
    # end function fail



    def streamer( self, message:str ):
        """
        Purpose : Stream the log info to server end
        Input   : log info
        Return  : none
        """
        try:
            send_sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            self.error( 'Failed to create socket object' )
        except Exception as e:
            self.error( str.format( 'Failed to create socket due to: ' +
                        'error {excp1}', excp1 = e ) )
        # end try

        sizeOfMessage = sys.getsizeof( message )

        if ( sizeOfMessage < LOG_DATAGRAM_SIZE_MAX ):
            message = message.encode('utf-8')

            try:
                send_sock.sendto( message, logs.clientAddress)
            except socket.error:
                self.error( str.format( 'Failed to stream info on host: {list1}',
                            list1 = logs.clientAddress ) )
            except Exception as e:
                self.error( str.format( 'Failed to stream info on host due to: ' +
                            'error {excp1}', excp1 = e ) )
            # end try
        else:
            choppedMsgList = []
            okSizeCharList = []
            for singChar in message:
                okSizeCharList.append( singChar )
                tempMsg = ''.join( okSizeCharList )

                if ( ( sys.getsizeof( tempMsg ) + 32 ) < LOG_DATAGRAM_SIZE_MAX ):
                    continue
                # end if

                choppedMsgList.append( tempMsg )
                okSizeCharList = [] # Reset the list char holder

            # end for

            lastMsg = ''.join( okSizeCharList )
            if ( lastMsg.strip() != '' ):
                choppedMsgList.append( lastMsg )
            # end if

            for choppedMsg in choppedMsgList:
                message = choppedMsg.encode('utf-8')
                try:
                    send_sock.sendto( message, logs.clientAddress)
                except socket.error:
                    self.error( str.format( 'Failed to stream info on host: {tup1}',
                                tup1 = logs.clientAddress ) )
                except Exception as e:
                    self.error( str.format( 'Failed to stream info on host due to: ' +
                                'error {excp1}', excp1 = e ) )
                # end try
            # end for
    # end function



    def __updateInfo( self ):
        """
        Purpose : Updates the stored values for class and function that called
                 the logger. Should call before every write to a log file
        Input   : None
        Return  : None
        """
        # get the previous frame ( method ) in order to get the
        # function and class name. two f_back due to consolidation
        # into one __updateInfo function
        cf = inspect.currentframe().f_back.f_back
        if 'self' in cf.f_locals:
            self.class_name = cf.f_locals[ 'self' ].__class__.__name__ + '.'
        # end if
        self.func_name = cf.f_code.co_name + '()'

        # for the classname...try just using class instead.
        # "{0}.{1}".format(a.__class__.__module__,a.__class__.__name__)
        #http://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance-in-python

        # this handles any function outside of the main function
        # that is not encapsulated by a class.
        if self.class_name == 'logs.':
            self.class_name = ""
        # end if

    # end function



    def processLoglevel( self, loglevel:int ):
        ''' Determines log flags based on loglevel int
        '''
        if   loglevel == 0:
            logs.output_screen_flag = False
            logs.output_debug_flag  = False
            logs.output_info_flag   = False
            logs.output_error_flag  = False
            logs.output_fail_flag   = False
        elif loglevel == 1:
            logs.output_screen_flag = True
            logs.output_debug_flag  = False
            logs.output_info_flag   = False
            logs.output_error_flag  = False
            logs.output_fail_flag   = False
        elif loglevel == 2:
            logs.output_screen_flag = True
            logs.output_debug_flag  = False
            logs.output_info_flag   = True
            logs.output_error_flag  = False
            logs.output_fail_flag   = False
        elif loglevel == 3:
            logs.output_screen_flag = True
            logs.output_debug_flag  = False
            logs.output_info_flag   = True
            logs.output_error_flag  = True
            logs.output_fail_flag   = False
        elif loglevel == 4:
            logs.output_screen_flag = True
            logs.output_debug_flag  = False
            logs.output_info_flag   = True
            logs.output_error_flag  = True
            logs.output_fail_flag   = True
        elif loglevel == 5:
            logs.output_screen_flag = True
            logs.output_debug_flag  = True
            logs.output_info_flag   = True
            logs.output_error_flag  = True
            logs.output_fail_flag   = True
        elif loglevel == 6:
            logs.output_screen_flag = False
            logs.output_debug_flag  = True
            logs.output_info_flag   = True
            logs.output_error_flag  = True
            logs.output_fail_flag   = True
        else:
            logs.output_screen_flag = True
            logs.output_debug_flag  = True
            logs.output_info_flag   = True
            logs.output_error_flag  = True
            logs.output_fail_flag   = True
        # end if
    # end function

# end class logs



def compress_file( fname, zname ) -> bool:
    """
    Purpose : Compress the log files
    Input   : filename and zipfilename
    Return  : True: Compressed
              False: failed to compressed
    """
    zipf = None

    try:
        zipf = zipfile.ZipFile( zname, 'a' )
        zipf.write( fname, arcname = os.path.basename( fname ) )
        zipf.close()
    except:
        print( 'log.compress_file: error: Failed to compress file ' +
                fname )
        return False
    # end try

    return True
# end function



def ziplogfiles( ) -> bool:
    log_file_list = []

    scriptAbsPath = logs.scriptAbsPath
    archivePath = os.path.join( scriptAbsPath, 'Archive')

    # Backing up existing logs
    print( 'Backing up existing log files please wait ...' )
    zip_file_name = os.path.join( archivePath, '{0}.zip'.format(
                        time.strftime( '%Y%m%d-%H%M%S' ) ) )

    log_file_list = [ logs.info_filename,  logs.debug_filename,
                      logs.error_filename, logs.fail_filename ]

    retvallist = get_resulttestinfo_fn()
    if ( retvallist is not None ):
        for retvalfn in retvallist:
            testinfofn = os.path.join( scriptAbsPath, retvalfn )
            log_file_list.append( testinfofn )
        # end for
    # end if

    for existing_file in log_file_list:
        if not os.path.isfile( existing_file ):
            continue
        # end if

        if ( compress_file( existing_file, zip_file_name ) == False ):
            print( 'Failed to compress file ' +
                   '{str1} to zip'.format( str1 = existing_file ) )
        # end if
    # end for
# end function



def get_resulttestinfo_fn() -> list:
    """ Read the line in info file which contains the test result filename
    """
    resfnlist = []
    targetfn = logs.info_filename
    infolog = ''
    infologlist = []
    searchstr = '{0}:'.format( LOG_TST_RES_FN )

    if ( os.path.isfile( targetfn ) == False ):
        print( 'Did not find the info log which we stored the filename for '
            'the test results' )
        return None
    # end if
    try:
        with open( targetfn, 'r') as fhandler:
            infolog = fhandler.read()
        # end file open
    except:
        print( 'Exception encountered while trying to read file {0}'.format(
            targetfn ) )
        return None
    # end try

    infologlist = infolog.split( '\n' )
    # Traverse in reverse order
    for i in range( 0, len( infologlist ) ):
        curline = infologlist[ ( len( infologlist ) - 1 ) - i ]
        if ( searchstr not in curline ):
            continue
        # end if

        curlinelist = curline.split( searchstr )
        laststr = curlinelist[ -1 ]

        laststr = str.strip( laststr )
        if ( laststr == '' ):
            continue
        # end if

        resfn = laststr
        
        resfnlist.append( resfn )
    # end if

    if ( len( resfnlist ) == 0 ):
        return None
    # end if

    return resfnlist
# end function



class FileStat(object):
    'Operation on file like get size,file time,compress etc..'

    def __init__( self, fname ):
        self.fname = fname
        self._stat = None



    def stat( self ):
        if self._stat is None:
            # Note: This will not update automatically if your file's stats change
            self._stat = os.stat( self.fname )
        return self._stat



    def datetime( self ):
        return datetime.datetime.fromtimestamp( self._stat.st_mtime )



    def age_in_days( self ):
        today = datetime.datetime.today()
        cday = self.datetime()
        return ( today - cday ).days



    def age_in_seconds( self ):
        today = datetime.datetime.today()
        cday = self.datetime()
        return ( today - cday ).seconds





def LogTestResultDatabase( dbInfo:dict, stationinfo: dict,
                           deviceinfo:dict, filelist:list ) -> int:
    '''From TestManager, store the completed test result into the database
    table. NOTE: Each result must have the key string in var BRD_SERIAL_NUM

    Filelist: List of filenames for each device test result

    Expectations:
        Packages:
            pymongo - Package should be installed. Installation
                      using pip or pip3 is suggested.
        Variables:
            log - Global variable log should be defined for logging purposes
        Modules:
            DatabaseManager.py - Module should be in the same directory
                                 as the calling module.

    Return:
        True - Did not encounter any issues when storing the result
        False - Issue where encountered when storing the result. Most likely
             the result was not stored.
    '''
    log.debug( 'Enter' )

    testResultList = []
    isIssues = False

    # Quick parameter check
    if ( len( filelist ) == 0 ):
        log.debug( 'Filename list parameter is empty. Nothing to store. ' +
                    'Exiting' )
        return DB_GENERAL_CFG
    # end if

    # Process the filelist and add dictionaries to var
    for fileNumber, filename in enumerate( filelist ):
        tempdict = None

        log.debug( str.format( 'Getting test result from ' +
                   'filename: {str1}', str1 = filename ) )

        # Using function read_json_file which returns OrderedDict
        tempdict = read_json_file( filename )
        if (type( tempdict ) == type( {} ) or
            type( tempdict ) == OrderedDict ):
            log.debug( str.format( 'utilities.read_json_file returned a ' +
                       'valid dictionary or OrderedDict for file ' +
                       '{str1}', str1 = filename ) )
        else:
            log.error( 'Skipping database store of result due to ' +
                        'failure when attempting to read file as JSON ' +
                        'with read_json_file( filename )' )
            isIssues = True
            continue
        # end if

        log.debug( 'Retrieved test result. Checking for serial '+
                    'number key' )

        # Check for serial number key or station id
        if ( ( not BRD_SERIAL_NUM in tempdict.keys() ) and
             ( not HW_STN_ID in tempdict.keys() ) ):
            log.error( str.format( 'Test result did not have the ' +
                        'required key {str1} or {str2}. Required for storing. ' +
                        'Skipping test result ' +
                        'store', str1 = BRD_SERIAL_NUM, str2 = HW_STN_ID ) )
            isIssues = True
            continue
        # end if

        # Embed the station info and device info dictionaries to the result
        try:
            tempdict[ RSLT_STN_INFO_KEY ] = stationinfo.copy()
        except AttributeError:
            # Possibility: "AttributeError: 'NoneType' object has no
            #    attribute 'copy'"
            log.error( 'Station info dictionary/OrderedDict is not defined' )
        except:
            log.error( 'Station info dictionary/OrderedDict access ' +
                       'encountered an issue' )
        # end try
        try:
            tempdict[ RSLT_DEV_INFO_KEY ] = deviceinfo.copy()
        except AttributeError:
            # Possibility: "AttributeError: 'NoneType' object has no
            #    attribute 'copy'"
            log.error( 'Device info dictionary/OrderedDict is not defined' )
        except:
            log.error( 'Device info dictionary/OrderedDict access ' +
                       'encountered an issue' )
        # end try

        testResultList.append( tempdict.copy() )
        if ( BRD_SERIAL_NUM in tempdict.keys() ):
            write_json_file(
                filename = '{0}_{1}_supertestresult.json'.format( tempdict[ BRD_SERIAL_NUM ],
                                                    stationinfo[ HW_STN_ID ] ),
                InfoDict = tempdict )
        else:
            write_json_file(
                filename = '{0}_supertestresult.json'.format( stationinfo[ HW_STN_ID ] ),
                InfoDict = tempdict )
        # end if

        log.info( '{0}: {1}'.format( LOG_TST_RES_FN, filename ) )
    # end for

    if ( isIssues == True ):
        log.error( 'Issues found in one or more device test result(s)' )
        return DB_GENERAL_CFG
    # end if

    # Finally before starting a database object, check for populated result
    #   list var
    if ( len( testResultList ) == 0 ):
        log.debug( 'Test result list is empty. Nothing to store. Verify' +
                    'the file content for proper key and or JSON ' +
                    'format. Exiting' )
        return DB_GENERAL_CFG
    # end if

    # Import database tool, we may want to add this section to the top
    #   like all other imports
    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return DB_GENERAL_CFG
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return DB_GENERAL_CFG
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        return DB_GENERAL_CONN
    else:
        log.debug( 'Connected to the database' )
    # end if

    # Store each result for each device
    for testResult in testResultList:
        if ( db.PutTestResult( Result = testResult.copy() ) != DB_INS_SUCCESS ):
            log.error( 'Failure in logging back test results to database!' )
            isIssues = True
        else:
            log.debug( 'Result store attempt successful' )
        # end if
    # end for

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( isIssues == True ):
        log.error( 'Issues found in one or more database store of test results' )
        return DB_INS_CFG
    # end if

    log.debug( 'Exit' )

    return DB_INS_SUCCESS
# end function LogTestResultDatabase





def UpdateTestStationDatabase( dbInfo:dict, testStationFileName: dict ) -> bool:
    '''From TestManager, update the station file

    testStationFileName: filename of the updated station info

    Expectations:
        Packages:
            pymongo - Package should be installed. Installation
                      using pip or pip3 is suggested.
        Variables:
            log - Global variable log should be defined for logging purposes
        Modules:
            DatabaseManager.py - Module should be in the same directory
                                 as the calling module.

    Return:
        True - Did not encounter any issues when storing the result
        False - Issue where encountered when storing the result. Most likely
             the result was not stored.
    '''
    log.debug( 'Enter' )

    isIssues = False

    log.debug( str.format( 'Updating test station info from filename: '
                           '{str1}', str1 = testStationFileName ) )

    # Using function read_json_file which returns OrderedDict
    stationInfo = read_json_file( testStationFileName )
    if (type( stationInfo ) == type( {} ) or
        type( stationInfo ) == OrderedDict ):
        log.debug( str.format( 'utilities.read_json_file returned a ' +
                   'valid dictionary or OrderedDict for file ' +
                   '{str1}', str1 = testStationFileName ) )
    else:
        log.error( 'Skipping database update of test station info due to ' +
                    'failure when attempting to read file as JSON ' +
                    'with read_json_file( filename )' )
        return DB_GENERAL_CFG
    # end if

    log.debug( 'Retrieved test station info. Checking for station '+
                'address key' )

    # Check for serial number key
    if ( not HW_STN_ID in stationInfo.keys() ):
        log.error( str.format( 'Test station did not have the ' +
                    'required key {str1}. Required for storing. ' +
                    'Skipping test station ' +
                    'store', str1 = HW_STN_ID ) )
        return DB_GENERAL_CFG
    # end if

    # Import database tool, we may want to add this section to the top
    #   like all other imports
    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return DB_GENERAL_CFG
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return DB_GENERAL_CFG
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        return DB_GENERAL_CONN
    else:
        log.debug( 'Connected to the database' )
    # end if

    if ( db.PutTestStation( TestStationDict = stationInfo.copy() ) != DB_INS_SUCCESS ):
        log.error( 'Failure in updating back test station to database!' )
        isIssues = True
    else:
        log.debug( 'Test station update attempt successful' )
    # end if

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( isIssues == True ):
        log.error( 'Issues found in one or more database store of test results' )
        return DB_INS_CFG
    # end if

    log.debug( 'Exit' )

    return DB_INS_SUCCESS
# end function UpdateTestStationDatabase





def getStationInfo( dbInfo:dict, StationId:str ) -> dict:

    log.debug( 'Enter' )

    returnDict = None

    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return returnDict
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return returnDict
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        returnBool = False
        return returnBool
    else:
        log.debug( 'Connected to the database' )
    # end if

    returnDict = db.GetTestStation( StationId = StationId )

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( type( returnDict ) == type( None ) ):
        log.error( 'database GetTestStation() failed!' )
    # end if

    log.debug( 'Exit' )

    return returnDict
# end function





def getDeviceInfo( dbInfo:dict, ProductId:str ) -> dict:

    log.debug( 'Enter' )

    returnDict = None

    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return returnDict
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return returnDict
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        returnBool = False
        return returnBool
    else:
        log.debug( 'Connected to the database' )
    # end if

    returnDict = db.GetTestSubjectByProductId( ProductId = ProductId )

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( type( returnDict ) == type( None ) ):
        log.error( 'database GetTestStation() failed!' )
    # end if

    log.debug( 'Exit' )

    return returnDict
# end function





def getDeviceTestResults( dbInfo:dict, SerialNumber:str ) -> list:

    log.debug( 'Enter' )

    returnDict = None

    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return returnDict
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return returnDict
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        returnBool = False
        return returnBool
    else:
        log.debug( 'Connected to the database' )
    # end if

    returnDictList = db.GetTestResults( SerialNumber = SerialNumber, MaxCount = None )

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    log.debug( 'Exit' )

    return returnDictList
# end function



def getSerialNumber( dbInfo:dict, CustomerId:str, 
        newtxrx_flag:bool ) -> dict:

    log.debug( 'Enter' )

    returnDict = None

    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return returnDict
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return returnDict
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        returnBool = False
        return returnBool
    else:
        log.debug( 'Connected to the database' )
    # end if

    if ( newtxrx_flag == True ):
        returnDict = db.GetSerialNumberForNewTxRx( 
                        CustomerId = CustomerId )
    else:
        returnDict = db.GetSerialNumber( CustomerId = CustomerId )
    # end if
    
    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( type( returnDict ) == type( None ) ):
        log.error( 'database GetTestStation() failed!' )
    # end if

    log.debug( 'Exit' )

    return returnDict
# end function



def getLaserTransmitterReceiver( dbInfo:dict, emcoretxrxid:str ) -> dict:

    log.debug( 'Enter' )

    returnDict = None

    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return returnDict
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return returnDict
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        returnBool = False
        return returnBool
    else:
        log.debug( 'Connected to the database' )
    # end if

    returnDict = db.GetLaserTransmitterReceiver( emcoretxrxid = emcoretxrxid )

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( type( returnDict ) == type( None ) ):
        log.error( 'database GetTestStation() failed!' )
    # end if

    log.debug( 'Exit' )

    return returnDict
# end function



def putSerialNumber( dbInfo:dict, serialnumberdict:str ) -> int:

    log.debug( 'Enter' )

    checkList = \
        [
            BRD_CUSTOMER_ID,
            BRD_MAN_DATE,
            BRD_EMKR_TX_RX_ID,
            BRD_EXISTING_CUST_REC
        ]
    isAKeyNotFound = False
    for eachKey in checkList:
        if ( eachKey not in serialnumberdict.keys() ):
            log.error( 'Required key {0} not found. Expected in Laser TX '
                       'dict'.format( eachKey ) )
            isAKeyNotFound = True
        # end if
    # end for

    if ( isAKeyNotFound == True ):
        return DB_GENERAL_CFG
    # end if

    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return DB_GENERAL_CFG
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return DB_GENERAL_CFG
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        return DB_GENERAL_CONN
    else:
        log.debug( 'Connected to the database' )
    # end if

    retCode = db.PutSerialNumber( serialnumberdict = serialnumberdict )

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( retCode != DB_INS_SUCCESS ):
        log.error( 'database PutLaserTransmitterReceiver() unsuccessful' )
    # end if

    log.debug( 'Exit' )

    return retCode
# end function



def putLaserTransmitterReceiver( dbInfo:dict, LaserTxRxDict:str ) -> int:

    log.debug( 'Enter' )

    checkList = \
        [
            BRD_EMKR_TX_RX_ID,
            HW_PRODUCT_ID,
            BRD_LASER_ID,
            BRD_PCBA_ID,
            BRD_ITU_CH_NUM,
        ]
    isAKeyNotFound = False
    for eachKey in checkList:
        if ( eachKey not in LaserTxRxDict.keys() ):
            log.error( 'Required key {0} not found. Expected in Laser TX '
                       'dict'.format( eachKey ) )
            isAKeyNotFound = True
        # end if
    # end for

    if ( isAKeyNotFound == True ):
        return DB_GENERAL_CFG
    # end if

    try:
        from automation1.DatabaseManager import Database
    except ImportError as e:
        log.error( str.format( 'PYMONGO is not installed. Please ' +
                    'install using pip ' +
                    '(pip install pymongo). {excp1}', excp1 = e ) )
        return DB_GENERAL_CFG
    except Exception as e:
        log.error( str.format( 'Exception occurred while attempting ' +
                    'to use DatabaseManager.py. Consider revising code ' +
                    'based on exception: {excp1}', excp = e ) )
        return DB_GENERAL_CFG
    # end try

    db = Database( dbInfo = dbInfo )

    # Connect to the database, if anything is wrong or we cannot connect
    #   the function will return false
    if not db.connect():
        log.error( 'DatabaseManager failed to connect to database cluster' )
        return DB_GENERAL_CONN
    else:
        log.debug( 'Connected to the database' )
    # end if

    retCode = db.PutLaserTransmitterReceiver( LaserTxRxDict = LaserTxRxDict )

    if not db.close():
        log.error( 'DatabaseManager failed to disconnect from the ' +
                    'database. May cause conflicts with resource ' +
                    'management' )
    else:
        log.debug( 'Disconnected successfully from the database' )
    # end if

    if ( retCode != DB_INS_SUCCESS ):
        log.error( 'database PutLaserTransmitterReceiver() unsuccessful' )
    # end if

    log.debug( 'Exit' )

    return retCode
# end function



# local variable
log = logs() # calling log calls as object
log.logger = os.path.basename(__file__)
