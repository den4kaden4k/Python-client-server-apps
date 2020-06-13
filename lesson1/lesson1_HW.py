# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

items_str = ['разработка', 'сокет', 'декоратор']
for item in items_str:
    print(item, type(item))
items_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                 '\u0441\u043e\u043a\u0435\u0442',
                 '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for item in items_unicode:
    print(item, type(item))

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

# items_byte = [b'class', b'function', b'method']
# for item in items_byte:
#     print(item, type(item), f'длина {len(item)}')

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

# items_for_byte = ['attribute', 'класс', 'функция', 'type']
# for item in items_for_byte:
#     try:
#         item = bytes(item, encoding='ascii')
#         print(f'{item} - можно записать в байтовом типе')
#     except UnicodeEncodeError:
#         print(f'{item} - невозможно записать в байтовом типе')

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

# items_enc = ['разработка', 'администрирование', 'protocol', 'standard']
# for item in items_enc:
#     item = item.encode('utf-8')
#     print(item)
#     item = item.decode('utf-8')
#     print(item)

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
# кириллице.

# import subprocess
# import chardet
#
# # args = ['ping', 'yandex.ru']
# args = ['ping', 'youtube.com']
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in subproc_ping.stdout:
#     coding = chardet.detect(line)
#     line = line.decode(coding['encoding'])
#     print(line)

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.

# lines = ['сетевое программирование', 'сокет', 'декоратор']
# with open('test_file.txt', 'w') as file:
#     for line in lines:
#         file.write(line + '\n')
# print(file)
# with open('test_file.txt', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')
