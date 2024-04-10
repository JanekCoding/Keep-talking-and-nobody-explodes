slowa = "alarm apacz arena babka cecha ekipa fajka farma głowa hańba larwa laska macka obiad palec palma pegaz robak scena skrót smoła smycz tafla teren toast torba trasa twarz walka wełna wnęka zakaz zwiad znicz żniwa "
rozl = slowa.split()

def program():

    filtered_list = rozl

    for i in range(5):
        lit1 = input(f"Podaj {i+1}. literę/litery:")
        pier = []
        for liter in lit1:
            pier.append(liter)

        wynik = []
        for j in pier:
            niemo = [word for word in filtered_list if len(word) > i and word[i] == j]
            wynik.extend(niemo)

        filtered_list = wynik
        print(filtered_list)

program()