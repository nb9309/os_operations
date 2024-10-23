import os
try:
    os.remove('prime_numbers.py')
    print('file removed')
except FileNotFoundError:
    print('file is not exist')