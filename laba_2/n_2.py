import csv
from operator import itemgetter

def write_csv(file_name: str, headers: list, data: list) -> None:
    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        exit("file not found")

try:
    lower_income = int(input("Enter lower income in range: "))
    higher_income = int(input("Enter higher income in range: "))
except ValueError:
    exit("enter integer please!!!")

if not (lower_income < higher_income):
    exit("enter valid range!!")

try:
    with open("countries.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        headers = reader.fieldnames
        countries = list(reader)
except FileNotFoundError or csv.Error as err:
    exit(f"Error: {err}")

inflation_sort = sorted(countries, key=itemgetter("Inflation"))
incomes = list(filter(lambda row: lower_income < float(row["Income"]) < higher_income, countries))

write_csv("incomes.csv", headers, incomes)
write_csv("sort_by_inflation.csv", headers, inflation_sort)
