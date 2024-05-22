from functools import reduce

liste = [1, 2, 3, 4, 5]

# filter
print(list(filter(lambda x: x%2, liste)))

# map
print(list(map(lambda x: x+1, liste)))

# reduce
print(reduce(lambda x, y: x+y, liste))