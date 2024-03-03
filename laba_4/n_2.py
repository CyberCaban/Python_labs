import collections
from operator import itemgetter
from pprint import pprint
from docxtpl import DocxTemplate
import csv

template = DocxTemplate("template.docx")

pages = [] # {Year, City, WinnerMale: time, WinnerFemale: time}

try:
    with open("data_marathon.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",", quoting=csv.QUOTE_ALL)
        marathones = list(reader)
except FileNotFoundError as err:
    exit(err)

ordered_by_year = collections.defaultdict(list)
for mar in marathones:
    ordered_by_year[mar["Year"]].append(mar)
pprint(ordered_by_year)
sort_by_year = sorted(marathones, key=itemgetter("Year", "Time", "City", "Sex"))
mmm = min(marathones, key=itemgetter("Time"))
# pprint(mmm)
# pprint(sort_by_year)