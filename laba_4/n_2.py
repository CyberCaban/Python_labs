import collections
from operator import itemgetter
from pprint import pprint
from docxtpl import DocxTemplate
import csv

def female_champ(value: list) -> dict:
    females = list(filter(lambda x: x["Sex"] == "Female", value))
    return min(females, key=itemgetter("Time"))


def male_champ(value: list) -> dict:
    males = list(filter(lambda x: x["Sex"] == "Male", value))
    return min(males, key=itemgetter("Time"))
    

try:
    with open("data_marathon.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",", quoting=csv.QUOTE_ALL)
        marathones = list(reader)
except FileNotFoundError as err:
    exit(err)

ordered_by_year = collections.defaultdict(list)
for mar in marathones:
    ordered_by_year[mar["Year"]].append(mar)

filtered = collections.defaultdict(list)
for key, value in ordered_by_year.items():
    try:
        filtered[key].append(female_champ(value))
    except ValueError:
        pass
    filtered[key].append(male_champ(value))
    
# pprint(filtered)

pages = [] # {Year, City, WinnerMale: time, WinnerFemale: time}
for k, v in filtered.items():
    pages.append({
        "Year": k,
        "City": ", ".join(set(map(lambda x: x["City"], v))),
        "WinnerMale": list(filter(lambda x: x["Sex"] == "Male", v)),
        "WinnerFemale": list(filter(lambda x: x["Sex"] == "Female", v))
    })
pprint(pages)
# print(temp)

template = DocxTemplate("template.docx")
template.render({"pages": pages})
template.save("res.docx")