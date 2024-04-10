def kolor_przycisk(kolor):
    if kolor == 'niebieski':
        napis = input("Wprowadź napis: ")
        if napis == 'przerwij':
            print("Przytrzymaj przycisk")
            kolor_paska = input("Wprowadź kolor paska: ")
            if kolor_paska == 'niebieski':
                print("Puść gdy licznik czasu wyświetla 4")
            elif kolor_paska == 'biały':
                print("Puść gdy licznik czasu wyświetla 1")
            elif kolor_paska == 'żółty':
                print("Puść gdy licznik czasu wyświetla 5")
            elif kolor_paska == 'inny':
                print("Puść gdy licznik czasu wyświetla 1")
                return
        else:
            liczba_baterii = input("Wprowadź liczbę baterii: ")
            if liczba_baterii in ['2', '3', '4', '5', '6', '7'] and napis == 'detonuj':
                print("Naciśnij i natychmiast puść przycisk")
                return
    elif kolor == 'biały':
        CAR = input("Świeci CAR? tak/nie: ")
        if CAR == 'tak':
            print("Przytrzymaj przycisk")
            kolor_paska = input("Wprowadź kolor paska: ")
            if kolor_paska == 'niebieski':
                print("Puść gdy licznik czasu wyświetla 4")
            elif kolor_paska == 'biały':
                print("Puść gdy licznik czasu wyświetla 1")
            elif kolor_paska == 'żółty':
                print("Puść gdy licznik czasu wyświetla 5")
            elif kolor_paska == 'inny':
                print("Puść gdy licznik czasu wyświetla 1")
                return

    liczba_baterii = input("Wprowadź liczbę baterii: ")
    if liczba_baterii in ['3', '4', '5', '6', '7']:
            FRK = input("Świeci FRK? tak/nie: ")
            if FRK == 'tak':
                print("Naciśnij i natychmiast puść przycisk")
                return
    elif kolor == 'żółty':
        print("Przytrzymaj przycisk")
        kolor_paska = input("Wprowadź kolor paska: ")
        if kolor_paska == 'niebieski':
            print("Puść gdy licznik czasu wyświetla 4")
        elif kolor_paska == 'biały':
            print("Puść gdy licznik czasu wyświetla 1")
        elif kolor_paska == 'żółty':
            print("Puść gdy licznik czasu wyświetla 5")
        elif kolor_paska == 'inny':
            print("Puść gdy licznik czasu wyświetla 1")
            return

    elif kolor == 'czerwony':
        napis = input("Wprowadź napis: ")
        if napis == 'przytrzymaj': print ( "naciśnij i natychmiast puść przycisk ")
        return

    else:
        kolor_paska = input( "Wprowadź kolor paska: ")
        if kolor_paska == 'niebieski':
            print("Puść gdy licznik czasu wyświetla 4")
        elif kolor_paska == 'biały':
            print("Puść gdy licznik czasu wyświetla 1")
        elif kolor_paska == 'żółty':
            print("Puść gdy licznik czasu wyświetla 5")
        elif kolor_paska == 'inny':
            print("Puść gdy licznik czasu wyświetla 1")
            return



kolor = input("Wpisz kolor przycisku: ")
kolor_przycisk(kolor)
