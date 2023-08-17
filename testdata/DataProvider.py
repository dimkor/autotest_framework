import json

my_file = open(file='test_data.json', mode='r', encoding='utf_8')
global_data = json.load(my_file)

class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get(self, prop: str) -> str:
        return self.data.get(prop)