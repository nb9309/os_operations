# rename file or folder

import os
try:
    os.rename('romove_file.py','remove_file.py')
    print('file renamed successfully')
except FileNotFoundError:
    print('check the  source file name')