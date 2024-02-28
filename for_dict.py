dict_brut = {"Alpha1": 0, "Alpha2": "DEF", "Alpha3": "GHI"}

print(dict_brut)

# Ittérer à travers clés et vals
for key, val in dict_brut.items():
    print(f"clé : {key}, val : {val}")

# Ittérer à travers clés
for key in dict_brut.keys():
    print(f"clé : {key}")

# Ittérer à travers vals
for val in dict_brut.values():
    print(f"val : {val}")

keys = list(dict_brut.keys())
vals = list(dict_brut.values())
print(keys, vals)