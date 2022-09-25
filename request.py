import csv

def request_number (key, meaning):
    with open('data.csv') as f:
        reader = csv.DictReader(f)
        for i in reader:
            if dict(i)[key] == meaning:
                print(i)