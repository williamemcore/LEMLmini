from distutils.core import setup
import py2exe
 
#setup(windows=["main2.py"])

setup(windows=[{"script": "main2.py"}],
      options= {"py2exe": {"includes": ["sip", "PyQt5.QtCore", "PyQt5.QtGui","serial.serialcli","cmd","code","pdb" ]}})
