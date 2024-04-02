price = 100 #global

def increment():
  price = 200
  result = price + 10
  print(result)
  return price

print(price)
price_2 = increment()
print(price_2)
print(result) # no va a funcionar porque esta llamando 
#una funcion con un scope local fuera de su contexto. 

