def cut_wire_3():
    red_wires = input("Czy są czerwone przewody? (tak/nie): ").lower() == "nie"
    if red_wires:
        print("Przetnij drugi przewód.")
    else:
        blue_wires = int(input("Ile niebieskich przewodów jest? "))
        if blue_wires > 1:
            print("Przetnij ostatni niebieski przewód.")
        else:
            print("Przetnij ostatni przewód.")


def cut_wire_4(serial_number):
    red_wires = int(input("Ile czerwonych przewodów jest? "))
    last_digit = int(serial_number[-1])
    yellow_wire_last = input("Czy ostatni przewód jest żółty? (tak/nie): ").lower() == "tak"
    blue_wires = int(input("Ile niebieskich przewodów jest? "))
    yellow_wires = int(input("Ile żółtych przewodów jest? "))

    if red_wires > 1 and last_digit % 2 != 0:
        print("Przetnij ostatni czerwony przewód.")
    elif yellow_wire_last and red_wires == 0:
        print("Przetnij pierwszy przewód.")
    elif blue_wires == 1:
        print("Przetnij pierwszy przewód.")
    elif yellow_wires > 1:
        print("Przetnij ostatni przewód.")
    else:
        print("Przetnij drugi przewód.")


def cut_wire_5(serial_number):
    black_wires = int(input("Ile czarnych przewodów jest? "))
    last_digit = int(serial_number[-1])
    red_wires = int(input("Ile czerwonych przewodów jest? "))
    yellow_wires = int(input("Ile żółtych przewodów jest? "))

    if "czarny" in serial_number and last_digit % 2 != 0:
        print("Przetnij czwarty przewód.")
    elif red_wires == 1 and yellow_wires > 1:
        print("Przetnij pierwszy przewód.")
    elif black_wires == 0:
        print("Przetnij drugi przewód.")
    else:
        print("Przetnij pierwszy przewód.")


def cut_wire_6(yellow_wires, serial_number):
    white_wires = int(input("Ile białych przewodów jest? "))
    red_wires = int(input("Ile czerwonych przewodów jest? "))

    if not yellow_wires and int(serial_number[-1]) % 2 != 0:
        print("Przetnij trzeci przewód.")
    elif yellow_wires and white_wires > 1:
        print("Przetnij czwarty przewód.")
    elif red_wires == 0:
        print("Przetnij ostatni przewód.")
    else:
        print("Przetnij czwarty przewód.")


def main():
    cables = int(input("Ile kabli jest? (3-6): "))

    if cables == 3:
        cut_wire_3()
    elif cables == 4:
        last_digit = input("Podaj ostatnią cyfrę numeru seryjnego kabli: ")
        cut_wire_4(last_digit)
    elif cables == 5:
        serial_number = input("Podaj numer seryjny kabli: ")
        cut_wire_5(serial_number)
    elif cables == 6:
        serial_number = input("Podaj numer seryjny kabli: ")
        yellow_wires = int(input("Ile żółtych przewodów jest? "))
        if yellow_wires == 1:
            cut_wire_6(True, serial_number)
        else:
            cut_wire_6(False, serial_number)
    else:
        print("Niepoprawna liczba kabli.")


if __name__ == "__main__":
    main()
