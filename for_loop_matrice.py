liste_brut = [["Bruno", "Sylvie", "Remy"], ["Plume", "Rose", "Antoine"], ["Christian", "Maud", "Albert"]]

for i, famille in enumerate(liste_brut):
    print(f"Famille {i+1} :")
    for nom in famille:
        print(f"    - {nom}")