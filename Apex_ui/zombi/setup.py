# Run 'python setup.py build' on cmd

import sys
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options = {
    'build_exe': {
        'include_files': [
            'car.jpg',
            'zombie.jpg',
            'space.png',
            'snakeimg.jpg',
            'search2.png',
            'mic2.png',
            'back1.png'
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('newvi.py')
]

setup(name='APEX',
      version='0.1',
      description='Python Game Demo',
      options=options,
      executables=executables
      )