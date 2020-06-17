import re
import os
import csv
from chardet import detect as detect


def get_data():
    target = {
        'Изготовитель системы': [],
        'Название ОС': [],
        'Код продукта': [],
        'Тип системы': [],
    }
    path = os.getcwd()
    files = os.listdir(path)
    for file in files:
        check = re.findall(r'info_\d+\.txt', file)
        if check:
            with open(check[0], 'rb') as file:
                string = file.read()
                encoding = detect(string)['encoding']
                string_decode = string.decode(encoding)
                for key in target.keys():
                    full_string = (re.findall(key + r':\s+.+\S', string_decode)).pop()
                    value_temp = re.split(':', full_string, maxsplit=1).pop()
                    value = re.findall(r'\b.+\S', value_temp).pop()
                    target[key] += [value]
    with open('main_data.txt', 'w', encoding='utf-8') as file:
        header = []
        main_data = []
        for key in target.keys():
            header.append(key)
        main_data.append(header)
        while True:
            values = []
            for key in header:
                temp = target[key].pop(0)
                values.append(temp)
            main_data.append(values)
            if not target[key]:
                break
        for line in main_data:
            file.write(str(line) + '\n')
        return main_data


def write_to_csv(name_file):
    with open(name_file, 'w', encoding='utf-8') as file:
        f_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        data = get_data()
        for row in data:
            f_writer.writerow(row)


name = 'report.csv'
write_to_csv(name)
