import json
from operator import itemgetter

with open("animals.json", "r") as file:
    data_animals = itemgetter("animals")(json.load(file))

birds = list(filter(lambda animal: animal["animal_type"] == "Bird", data_animals))
diurnal = list(filter(lambda animal: animal["active_time"] == "Diurnal", data_animals))
min_weight = min(data_animals, key=itemgetter("weight_min"))

print(birds)
print("=============================================")
print(diurnal)
print("=============================================")
print(min_weight)