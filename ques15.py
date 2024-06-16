import csv
with open("C:/Users/anshi/Downloads/train.csv - train.csv.csv", mode = 'r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)