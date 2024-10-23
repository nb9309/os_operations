# create folder hieararcy
# we can create folder in folder at a time
import os

try:
    os.makedirs('india\\ap\\mopidevi\\kothapalem')
    print('folder hierarcy created')
except FileExistsError:
    print('folder alredy exist')