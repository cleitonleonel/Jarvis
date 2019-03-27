import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:\\Python35\\tcl\\tcl8.6'

os.environ['TK_LIBRARY'] = 'C:\\Python35\\tcl\\tk8.6'

setup(
    name="Jarvis Speech EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("ana_speech.py")])