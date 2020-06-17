import yaml

data_to_yaml = {
    '1€': ['value_1', 'value_2'],
    '2€': 777,
    '3€': {'key1': 'value_1', 'key2': 'value_2'}
}
with open('file.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data_to_yaml, file, default_flow_style=False, allow_unicode=True)
