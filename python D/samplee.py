import csv
with open("Downloads/ss2.csv",'r')as file:
    reader=csv.reader(file,determination="\t")
    for now in reader:
        print(row)
