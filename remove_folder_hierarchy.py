# removing folder hierarchy
import os
try:
    os.removedirs('python\\naresh')
    print('folders rempoved')
except FileNotFoundError:
    print('file was not existed')
except OSError:
    print('check folder empty or not')

