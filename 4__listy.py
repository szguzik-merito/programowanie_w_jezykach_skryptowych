# Lista [] - jest edytowalna/manipulowalna/mutowalna
#Indexy_listy 0,1,2,3,4
first_list = [1,2,3,4,5]
print('Wypisywanie listy')
print(first_list)

# wypisywanie po indexie - po kluczu - kluczu niejawnym
print('wypisywanie po indexie - po kluczu - kluczu niejawnym') 
print(first_list[3]) 

# dodawanie elementow do listy
first_list.append(66)
print('dodawanie elementow do listy')
print(first_list)

# aktualizacja
first_list[3] = 44
print('aktualizacja')
print(first_list)

# odwracanie listy
print('odwracanie listy')
print(first_list[::-1])

# Usuwanie po indexie / kluczu
del first_list[2]
print(first_list)

# Nowa tablica 
second_list = [1,'Kasia', 'Kasia',3,4,5]
print(second_list)
# Usuwanie z listy przez value
second_list.remove('Kasia')
print(second_list)