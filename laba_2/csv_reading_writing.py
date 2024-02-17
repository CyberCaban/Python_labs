import csv
from pprint import pprint

films = []

with open('film.csv', 'r') as csvfile:
    # формируем объект reader (список строк)
    reader = csv.reader(csvfile, delimiter=';')
    # пропускаем строку заголовков
    reader.__next__()
    # итерируемся по остальному содержимому
    for row in reader:
        if '' not in row:
            films.append(row)

pprint(films)

with open('filtred_films.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # записываем заголовки
    writer.writerow(['Year', 'Length', 'Title', 'Subject', 'Actor', 'Actress', 'Director', 'Popularity', 'Awards', 'Image'])
    # записываем всё остальное
    for film in films:
        writer.writerow(film)
