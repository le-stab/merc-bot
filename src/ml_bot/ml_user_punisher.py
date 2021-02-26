
from operator import itemgetter, attrgetter
import requests
user = 'ORSLOK400'
api_url = f'https://api.mercadolibre.com/sites/MLA/search?nickname={user}'

r = requests.get(api_url)
json = r.json()

products = []

for item in json['results']:
    products.append([item['title'], item['price'], item['sold_quantity'], item['permalink']])

sorted_products = sorted(products, key=itemgetter(2), reverse=True)

for item in sorted_products:
    if item[2] != 0:
        print(item)
