import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as file:
        obj = json.load(file)
    dict_to_json = dict(товар=item, количество=quantity, цена=price, покупатель=buyer, дата=date)
    with open('orders.json', 'w', encoding='utf-8') as file:
        new_list = obj['orders']
        new_list.append(dict_to_json)
        obj['orders'] = new_list
        json.dump(obj, file, indent=4)


write_order_to_json('стул', 77, 5500, 'Иванов Иван', '17-06-2020')
# with open('orders.json', encoding='utf-8') as file:
#     obj = json.load(file)
#     for key, value in obj.items():
#         print(f'{key} : {value}')
