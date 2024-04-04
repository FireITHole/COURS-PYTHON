list_classes = [["un", "deux"], ["un", "deux", "trois"], ["quatre"]]

""" for liste in list_classes:
    for element in liste:
        print(element)

for index_liste in range(len(list_classes)):
    for index_element in range(len(list_classes[index_liste])):
        print(list_classes[index_liste][index_element]) """


def liste_imbrique(liste: list, count=0) -> int:
    if len(liste) == 0:
        return count
    
    if type(liste[0]) is list:
        count += liste_imbrique(liste[0])

    return liste_imbrique(liste[1:], count + 1)

def deep_count(a):
    result = 0
    for i in range(len(a)):
        if type(a[i]) is list:
            result += deep_count(a[i])
        result += 1
    return result

print(liste_imbrique(list_classes))