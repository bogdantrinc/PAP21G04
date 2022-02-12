import sys
from clasa_standard import Standard
from clasa_premium import Premium


def signup():   # creeaza un cont nou
    print("  Sign up for a Pay Account  ".center(50, "*"))
    print("  1. Pay Standard  ".center(55))
    print("  2. Pay Premium  ".center(53))
    optiune = input("Alege o optiune din meniu: ")
    if optiune == '1':
        return Standard.signup()
    elif optiune == '2':
        return Premium.signup()
    print("  EROARE! Optiunea nu exista.  ".center(50, "#"))


def conectare(user):    # meniul profilului, dupa ce utilizatorul s-a conectat
    while True:
        print(f'  Welcome, {user.prenume}!  '.center(50, "*"))
        print("  1. Profile  ".center(50))  # vizionare profil
        print("  2. Top-Up  ".center(50))  # adauga bani in cont
        print("  3. Marketplace  ".center(53))  # cheltui bani
        print("  4. Transferuri (Pay Premium)  ".center(67))
        print("  5. Exit  ".center(47))
        print("".center(50, "*"))
        optiune = input("Alege o optiune din meniu: ")
        if optiune == '1':
            user.afisare()
        elif optiune == '2':
            if user.adauga_bani() is None:
                continue
        elif optiune == '3':
            if user.cheltuie() is None:
                continue
        elif optiune == '4':
            if Premium.transferuri(user) is None:
                continue
        elif optiune == '5':
            break
        else:
            print("  EROARE! Optiunea nu exista.  ".center(50, "#"))


def login():    # logare in cont pt. a intra in meniul profilului
    print("  Login into your Pay Account  ".center(50, "*"))
    print("  1. Pay Standard  ".center(55))
    print("  2. Pay Premium  ".center(53))
    optiune = input("Alege o optiune din meniu: ")
    if optiune == '1':
        user = Standard.login()
    elif optiune == '2':
        user = Premium.login()
    else:
        print("  EROARE! Optiunea nu exista.  ".center(50, "#"))
        return None
    print("".center(50, '='))
    if user is None:
        return None
    if optiune == '1' and type(user) is Standard:
        return conectare(user)
    elif optiune == '2' and type(user) is Premium:
        return conectare(user)
    else:
        print(f"  EROARE! Contul nu corespunde.  ".center(50, "#"))


meniu_principal = {
    '1': signup,
    '2': login,
    '3': sys.exit,
    '4': Premium.afisare_banca   # interfata de administrare a bancii care afiseaza toti utilizatorii
}
########################################################################################################
test_1 = Standard("John", "Doe", "0773847296")
Standard.lista_utilizatori.append(test_1)
test_2 = Premium("Ion", "Dorel", "0773847297")
Premium.lista_utilizatori.append(test_2)
########################################################################################################

# MAIN

if __name__ == "__main__":
    while True:
        print("  Pay  ".center(50, "*"))
        print("  1. Sign up  ".center(50))  # inregistrare in aplicatie
        print("  2. Login  ".center(47))  # logare cu nr. de telefon
        print("  3. Exit  ".center(47))
        print("  4. Administrare  ".center(55))  # interfata de administrare a bancii
        print("".center(50, "*"))
        optiune = input("Alege o optiune din meniu: ")
        if optiune in meniu_principal:
            meniu_principal[optiune]()
        else:
            print("  EROARE! Optiunea nu exista.  ".center(50, "#"))
