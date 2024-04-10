def program():
    def znajdz_y(x):
        if x in ['cngl', 'cnlg', 'clng', 'clgn', 'cgln', 'cgnl', 'ncgl', 'nclg', 'nglc', 'ngcl', 'nlcg', 'nlgc', 'lcng', 'lcgn', 'lngc', 'lncg']:
            y = n
        elif x in ['cng', 'gnc', 'ngc', 'cgn', 'gcn', 'ncg']:
            y = r
        elif x in ['cnl', 'lcn', 'ncl', 'nlc', 'lnc', 'cln']:
            y = s
        elif x in ['cgl', 'cgl', 'lcg', 'lgc', 'gcl', 'glc']:
            y = b
        elif x in ['ngl', 'gnl', 'lng', 'lgn', 'gln', 'nlg']:
            y = r
        elif x in ['cn', 'nc']:
            y = s
        elif x in ['cg', 'gc']:
            y = p
        elif x in ['cl', 'lc']:
            y = b
        elif x in ['ng', 'gn']:
            y = n
        elif x in ['nl', 'ln']:
            y = r
        elif x in ['gl', 'lg']:
            y = b
        elif x == 'c':
            y = s
        elif x == 'n':
            y = s
        elif x == 'g':
            y = p
        elif x == 'l':
            y = n
        else:
            y = 'Nieznana wartość'
        return y

    p = "PRZETNIJ PRZEWÓD"
    n = "NIE PRZECINAJ PRZEWODU"
    s = "PRZETNIJ PRZEWÓD JEŚLI OSTATNIA CYFRA NUMERU SERYJNEGO JEST PARZYSTA"
    r = "PRZETNIJ PRZEWÓD JEŚLI BOMBA MA PORT RÓWNOLEGŁY"
    b = "PRZETNIJ PRZEWÓD JEŚLI BOMBA MA 2 LUB WIĘCEJ BATERII"

    x = input("Podaj literki c = czerwony n = niebieski g = gwiazdka l = led: ")
    wynik = znajdz_y(x)
    print("Dla", x, "to", wynik)
    if x != "end":
        program()

program()