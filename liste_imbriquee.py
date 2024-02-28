list_classes = [["un", "deux"], ["un", "deux", "trois"], ["quatre"]]

for liste in list_classes:
    for element in liste:
        print(element)

for index_liste in range(len(list_classes)):
    for index_element in range(len(list_classes[index_liste])):
        print(list_classes[index_liste][index_element])