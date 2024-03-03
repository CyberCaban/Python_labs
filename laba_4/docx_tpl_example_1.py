# для установки pip install docxtpl
from docxtpl import DocxTemplate
import datetime as dt

template = DocxTemplate("template_1.docx")

team = input("Введите название команды: ")

names = []

print("Введите имена участников команды (каждое имя с новой строки, пустая строка - окончание ввода): ")
name = "name"
while name:
    name = input()
    names.append(name)

context = {
    'team': team,
    'names': names,
    'date': dt.date.today()
}

template.render(context)
template.save("res.docx")
