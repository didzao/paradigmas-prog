import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    'include_files': [
        'font', 'sound', 'sprites',
        'settings.py', 'tetris.py', 'tetromino.py',
    ]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Tetris",
    version="1.0",
    description="Jogo de tetris",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="main.py", base=base)]
)
