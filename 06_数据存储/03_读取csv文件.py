import csv

with open('../temp/csv_output.csv', 'r', encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
        print(row[0])
