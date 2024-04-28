from operator import itemgetter
from collections import Counter
import csv
import numpy as np

with open("udemy_courses.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    courses = list(reader)
    headers = reader.fieldnames


prices = list(map(int, map(itemgetter("price"), courses)))
subscriber_count = list(map(int, map(itemgetter("num_subscribers"), courses)))
content_duration = list(map(float, map(itemgetter("content_duration"), courses)))
lvls = list(map(itemgetter("level"), courses))

median = np.median(prices, axis=0)
min_sub = np.amin(subscriber_count, axis=0)
max_dur = np.amax(content_duration, axis=0)
levels = Counter()
for lvl in lvls:
    levels[lvl] += 1
levels = max(levels, key=levels.get)
print("Median: ", median)
print("Min sub: ", min_sub)
print("Max dur: ", max_dur)
print("Most courses level: ", levels)
