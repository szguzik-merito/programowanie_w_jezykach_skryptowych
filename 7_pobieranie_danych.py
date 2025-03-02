# lista studentwów
students = ["Jan Kowalski", "Monika Wisniewska"] 
# Pobieranie danych od uzytkownika
imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
wiek = input("Podaj swoj wiek: ")
wiek = int(wiek)
# konkatenacja
newstudent = imie + ' ' + nazwisko
students.append(newstudent)
# wypisywanie danych
print("Twoje imie to: {} {}".format(imie, nazwisko))
print("Nowa lista studentów to", students)

if wiek <= 20:
    print("Jesteś młody")
elif(wiek >= 21 and wiek <= 30):
    print("No już nie taki młody")
else:
    print("No masz juz troche lat")    
    