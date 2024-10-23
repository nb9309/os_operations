# creating a folder
# we can create one folder at a time only
import os
try:
    os.mkdir('naresh\\prime_numbers.py')
    print('folder created')
except FileExistsError:
    print('file alredy exist')