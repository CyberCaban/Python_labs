import json
from operator import itemgetter
from pprint import pprint

try:
    with open("animals.json", "r") as file:
        data_animals = itemgetter("animals")(json.load(file))
except FileNotFoundError or json.JSONDecodeError as err:
    exit(f"{err}")

birds = list(filter(lambda animal: animal["animal_type"] == "Bird", data_animals))
diurnal = len(list(filter(lambda animal: animal["active_time"] == "Diurnal", data_animals)))
min_weight = min(data_animals, key=itemgetter("weight_min"))

pprint(birds)
print("=" * 40)
print(diurnal)
print("=" * 40)
pprint(min_weight)