# removing single folder
import os
try:
    os.rmdir('india\\ap\\kothapalem')
    print('folder removed')
except FileNotFoundError:
    print('file is not exist')
except OSError:
    print('check file empty or not')
