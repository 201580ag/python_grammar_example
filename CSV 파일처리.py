import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 25])
    writer.writerow(["Alice", 30])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
