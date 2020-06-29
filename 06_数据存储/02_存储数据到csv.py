import csv

output_list = ['1', '2', '3', '4']
with open('../temp/csv_output.csv', 'w', encoding='UTF-8', newline='') as csv_file:
    w = csv.writer(csv_file)
    w.writerow(output_list)
