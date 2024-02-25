import json
from operator import itemgetter

try:
    with open("animals.json", "r") as file:
        data_animals = itemgetter("animals")(json.load(file))
except FileNotFoundError:
    exit("file not found")

birds = list(filter(lambda animal: animal["animal_type"] == "Bird", data_animals))
diurnal = len(list(filter(lambda animal: animal["active_time"] == "Diurnal", data_animals)))
min_weight = min(data_animals, key=itemgetter("weight_min"))

print(birds)
print("=" * 40)
print(diurnal)
print("=" * 40)
print(min_weight)