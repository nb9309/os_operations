import csv
column = ['name','job','sal']
records = [['nares','software',40000],['sukesh','hardware',30000]]

with open('C:\\Users\\nares\\PycharmProjects\\os_operations\\naresh\\prime_numbers.py\\java.csv','a') as fp:
    obj = csv.writer(fp)
    obj.writerow(column)
    obj.writerows(records)
    print('file created')