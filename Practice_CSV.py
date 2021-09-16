import csv
user_list = [{'name':'Маша', 'age': 25, 'job': 'scientist'},
             {'name':'Вася', 'age': 8, 'job': 'Programmer'},
             {'name':'Эдуард', 'age': 48, 'job': 'Big boss'},
             {'name':'Арагорн', 'age': 87, 'job': 'Наследник Исилдура'}
             
    ]

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']# названия столбцов
    writer = csv.DictWriter(f, fields, delimiter = ';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)