import cx_Freeze
import os
import sys

base = None

if sys.platform == "win64":
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ITAPP03\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ITAPP03\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("face_recognition_app.py", base=base)]

cx_Freeze.setup(
    name="Contactless Facial Recognition System",
    options={"build_exe": {"packages": ["kivy", "os"],
                           "include_files": ['tcl86t.dll', 'tk86t.dll', 'assest', 'imageData','cx_Freeze-6.9-cp310-cp310-win_amd64.whl']}},
    version="1.0",
    description="Contactless Attendance System",
    author= "Hamsuky-developer",
    executables=executables
)
