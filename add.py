import csv

table = ['last_name', 'name', 'fone_number', 'city']

def add_directory ():
    record = [input (f'{i} :') for i in table]
    
    with open('data.csv', 'a') as f:
         writer = csv.writer(f)
         writer.writerow(record)