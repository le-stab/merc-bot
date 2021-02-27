
import requests
import json


user = 'ORSLOK400'
api_url = f'https://api.mercadolibre.com/sites/MLA/search?nickname={user}'

r = requests.get(api_url)
json_data = json.loads(r.text)

products = []

# print(json.dumps(json_data, indent=2))

for item in json_data['results']:
    products.append([item['title'], item['price'], item['id'], item['sold_quantity'], item['permalink']])

sorted_products = sorted(products, key=lambda x: x[2], reverse=True)

for item in sorted_products:
    if item[2] != 0:
        print(item)
