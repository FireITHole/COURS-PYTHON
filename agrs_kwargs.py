def somme(*args):
    return sum(args)

def print_values(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")

print(somme(2, 3, 4, 5, 6))
print_values(test=1, autre_test=2)
