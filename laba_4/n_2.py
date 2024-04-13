import collections
from operator import itemgetter
from pprint import pprint
from docxtpl import DocxTemplate
import csv

try:
    with open("data_marathon.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",", quoting=csv.QUOTE_ALL)
        marathons = list(reader)
except FileNotFoundError as err:
    exit(err)

cities = set()
ordered_by_year = collections.defaultdict(list)
for mar in marathons:
    cities.add(mar["City"])
    ordered_by_year[mar["Year"]].append(mar)

# pprint(cities)

filtered = collections.defaultdict(lambda: collections.defaultdict(list))
for key, value in ordered_by_year.items():
    for champ in value:
        for city in cities:
            if champ["City"] == city:
                filtered[key][city].append([champ["Sex"], champ["FullName"]])

pprint(filtered)

pages = []  # {Year, City, WinnerMale: time, WinnerFemale: time}

template = DocxTemplate("template.docx")
template.render({"pages": filtered})
template.save("res.docx")
