def verificare_litere(valoare: str):    # verifica inputul nume si prenume
    while True:
        if valoare.isalpha() is False:
            print("  EROARE! Va rugam introduceti doar LITERE.  ".center(50, "#"))
            valoare = input("Introduceti o optiune valida: ")
        else:
            return valoare.capitalize()


def verificare_float(valoare: str):    # verifica inputul suma
    while True:
        try:
            valoare = float(valoare)
        except ValueError:
            print("  EROARE! Se accepta doar NUMERE.  ".center(50, "#"))
            valoare = input("Suma: ")
        else:
            return abs(round(valoare, 2))


def verificare_telefon(valoare: str):   # verifica inputul telefon
    while True:
        if valoare.startswith('0') and len(valoare) == 10 and valoare.isnumeric() is True:
            return valoare
        else:
            print('  EROARE! Numar invalid.  '.center(50, "#"))
            valoare = input("Telefon: ")


def verificare_moneda(valoare: str):    # verifica inputul moneda
    dictionar_monede = {
        'USD': 0,
        'EUR': 0,
        'BTC': 0
    }
    while True:
        if valoare.upper() in dictionar_monede.keys():
            return valoare.upper()
        else:
            print("  EROARE! Moneda nu exista.  ".center(50, "#"))
            valoare = input("Moneda (USD/EUR/BTC): ").upper()


def verificare_optiune(valoare: str):   # verifica inputul y/n
    while True:
        if valoare not in ['y', 'n']:
            print("  EROARE! Optiunea nu exista.  ".center(50, "#"))
            valoare = input("Introduceti o optiune valida: ")
        else:
            return valoare
