import csv
import requests

def examples():
    '''example variables'''
    a = 5.67890
    b = "hello"
    c = [*range(1,5)]
    b = b.capitalize()
    return a, b, c

def open_close():
    '''open a file and closing statement'''
    csvfile = open('data/addresses.csv')
    doc_content = csv.reader(csvfile)
    for row in doc_content:
        print(row)
    csvfile.close()

def with_open():
    '''open file with "with statement"'''
    with open('data/addresses.csv') as csvfile:
        doc_content = csv.reader(csvfile)
        for row in doc_content:
            print(row[0], row[1])

def open_with_heathers():
    with open('data/biostats.csv') as csvfile:
        doc_content = csv.DictReader(csvfile,skipinitialspace=True )
        for row in doc_content:
            print(row["Name"], row['Age'])

def writing_csv(data):
    with open('data/new.csv', 'w') as csvfile:
        doc_content = csv.DictWriter(csvfile, fieldnames=data[0].keys(), delimiter = " ")
        print("creating column names")
        doc_content.writeheader()
        for row in data:
            print(f"saving {row['first_name']}")
            doc_content.writerow(row)



if __name__ == '__main__':
    '''entrypoint, commands from the terminal'''
    # open_close()
    # with_open()
    # open_with_heathers()

    beatles = [
        { 'first_name': 'John', 'last_name': 'lennon', 'instrument': 'guitar'},
        { 'first_name': 'Ringo', 'last_name': 'Starr', 'instrument': 'drums'}
    ]
    writing_csv(beatles)
