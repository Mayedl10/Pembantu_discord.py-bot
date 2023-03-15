import json

data = [{"name":"Copper Role","price":1000,"description":"Role"},
            {"name":"Gold Role","price":10000,"description":"Role"},
            {"name":"Diamond Role","price":1000000,"description":"Role"},
            {"name":"Banana","price":69696969,"description":"A delicious banana!"}]

with open('mainshop.json', 'w') as fout:
    json.dump(data, fout)
