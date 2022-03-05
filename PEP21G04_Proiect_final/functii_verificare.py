import datetime


def verificare_nume(valoare: str):   # Verifica numele complet
    nume_prenume = valoare.split(' ')
    if len(nume_prenume) == 2 and nume_prenume[0].isalpha() and nume_prenume[1].isalpha():
        return nume_prenume[0].capitalize() + ' ' + nume_prenume[1].capitalize()
    else:
        print("    EROARE! Format incorect!    ".center(100, '#'))
        valoare = input('Format corect "Nume Prenume": ')
        return verificare_nume(valoare)


def verificare_denumire(valoare: str):   # Verifica denumirile de departamente, functii, etc.
    if valoare.replace(" ", "").isalpha():
        return valoare
    else:
        print("    EROARE! Format incorect!    ".center(100, '#'))
        valoare = input('Introduceti doar litere: ')
        return verificare_denumire(valoare)


def verificare_data(valoare: str):    # Verifica data
    data_ang = valoare.split("-")
    try:
        data_ang = datetime.date(int(data_ang[0]), int(data_ang[1]), int(data_ang[2]))
    except Exception:
        print("    EROARE! Format incorect!    ".center(100, '#'))
        valoare = input('Format corect "aaaa-ll-zz": ')
        return verificare_data(valoare)
    else:
        return data_ang


def verificare_salar(valoare: str):    # Verifica salariul
    try:
        valoare = float(valoare)
    except ValueError:
        print("  EROARE! Se accepta doar NUMERE.  ".center(100, "#"))
        valoare = input("Salar: ")
        return verificare_salar(valoare)
    else:
        return abs(round(valoare, 2))
