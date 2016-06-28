import sys
from cx_Freeze import setup, Executable

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Monitora Temperatura",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Monitora Temperatura.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}
build_exe_options = {"packages": ["os", "pandas", "threading", "sys", "serial", "subprocess", "pyqtgraph"], "include_files": ["View\\", "Controle\\", "Util\\", "Model\\"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Monitora Temperatura",
        version = "0.1",
        description = "Monitora a temperatura da caixa.",
        options = {"build_exe": build_exe_options,"bdist_msi": bdist_msi_options},
        executables = [Executable("main_app.py", base=base)])
