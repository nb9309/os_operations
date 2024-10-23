# find number of directarys

import os

a = os.listdir()
print('number of directarys: ',len(a))
print('-'*20)

count = 0
for i in a:
    if i.endswith('.py'):
        print(i)
        count += 1

print('-'*20)
print(count)