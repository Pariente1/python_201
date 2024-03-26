from typing import Text


def find_volume(lenght=1, width=1, depth=1,a=0):
  return lenght* width * depth, width, 'hola', a

result, width, text, a = find_volume(width=10)
print(result)
print(width)
print(text)
print(a)