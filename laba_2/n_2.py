import csv
from pprint import pprint

try:
    lower_income = int(input("Enter lower income in range: "))
    higher_income = int(input("Enter higher income in range: "))
except ValueError:
    print("enter integer please!!!")
    exit()

incomes = []
headers = []
with open("countries.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    headers = reader.fieldnames
    for row in reader:
        if lower_income < float(row["Income"]) and higher_income > float(row["Income"]):
            incomes.append(row)

with open("incomes.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    writer.writerows(incomes)
    