items = [
  {
    'product': 'camisa',
    'price': 100
    
  },
  {
    'product': 'pantalones',
    'price' : 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda i:i['price'], items))

print(prices)

def add_taxes(item):
  new_item = item.copy()
  new_item['taxes'] = item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print(new_items)