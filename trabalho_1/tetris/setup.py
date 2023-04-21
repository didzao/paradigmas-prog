import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="Tetris game",
    options={'build_exe': {'packages': ['pygame'],
                           'include_files': ['assets/audio', 'assets/font',
                                             'assets/sprites', 'settings.py',
                                             'tetris.py', 'tetromino.py']}},

    executables=executables

)
