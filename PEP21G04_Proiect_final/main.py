import sys
from functii_verificare import *
from Angajati import Angajat
from Departament import Departament


def vizualizare():
    """
    Functie care corespunde primei optiuni din meniul principal. Functia va include 3 optiuni:
    1. Vizualizare a tuturor angajatiilor in functie de departament.
        -- apeleaza functia afisare_angajati() din clasa Angajat

    2. Vizualizare a angajatiilor de pe un singur departament. Exemplu:

        Introduceti departamentul: hr
        ---------------
        Nume: Maria Popescu
        Functie: Manager
        Data angajarii: 2020-7-12
        Salar: 7600 lei
        ---------------
        Nume: x
        Functie: y
        Data angajarii: xx-x-xx
        Salar: xxxx lei

    3. Iesire la meniul principal.

    """
    print("    Vizualizare    ".center(100, '='))
    print("    1. Vizualizare a tuturor angajatiilor in functie de departament    ".center(100))
    print("    2. Vizualizare a angajatiilor de pe un singur departament    ".center(93))
    print("    3. Iesire    ".center(45))
    print("".center(100, '='))
    optiune = input("Introduceti optiune: ")
    if optiune == '1':
        print("    Vizualizare a tuturor angajatiilor in functie de departament    ".center(100, '='))
        Angajat.afisare_angajati()
        return vizualizare()
    elif optiune == '2':
        print("    Vizualizare a angajatiilor de pe un singur departament    ".center(100, '='))
        Angajat.afisare_departament(verificare_denumire(input("Introduceti departamentul: ")))
        return vizualizare()
    elif optiune == '3':
        return None
    else:
        print("    EROARE! Optiunea nu exista.    ".center(100, '#'))
        return vizualizare()


def informatii_firma():
    """
    Functie care corespunde optiunii 2 din meniul principal. Contine un meniu cu 3 optiuni:
    1. Afisare medie salariala
    2. Afisare nr de anagajati/ departament
    3. Afisare cati angajati au vechime mai mare de x ani.
    4. Iesire
    """
    print("    Informatii despre firma    ".center(100, '='))
    print("    1. Afisare medie salariala    ".center(93))
    print("    2. Afisare nr de angajati/ departament    ".center(106))
    print("    3. Afisare numar de angajati cu vechime mare mare de x ani    ".center(125))
    print("    4. Iesire    ".center(77))
    print("".center(100, '='))
    optiune = input("Introduceti optiune: ")
    if optiune == '1':
        print("    Afisare medie salariala    ".center(100, '='))
        suma = sum([om.salar for om in Angajat.angajati])
        print(f"Media salariala este: {round(suma/len(Angajat.angajati), 2)} Lei")
        print("".center(100, '='))
        return informatii_firma()
    elif optiune == '2':
        print("    Afisare nr de angajati/ departament    ".center(100, '='))
        for dep in Departament.departamente:
            # creeaza o lista cu departamentul fiecarui angajat
            posturi_departamente = [om.nume_dep.upper() for om in Angajat.angajati]
            # retine lungimea listei filtrate care contine doar angajatii departamentului curent
            nr_locuri = len(list(filter(lambda post: post == dep.nume_dep.upper(), posturi_departamente)))
            print(f"{dep.nume_dep}: {nr_locuri} angajati")
        print("".center(100, '='))
        return informatii_firma()
    elif optiune == '3':
        print("    Afisare numar de angajati cu vechime mare mare de x ani    ".center(100, '='))
        # retine vechimea ceruta in zile
        try:
            input_user = int(input("Introduceti vechimea dorita: "))
        except Exception:
            print("    EROARE! Format incorect!    ".center(100, '#'))
            return informatii_firma()
        else:
            input_user = input_user * 365
        # creaza o lista cu vechimea angajatilor in zile
        lista_timp = [(datetime.date.today() - om.data_angajarii).days for om in Angajat.angajati]
        # retine lungimea listei filtrate cu vechimea care respecta cererea
        nr_angajati = len(list(filter(lambda vechime: vechime > input_user, lista_timp)))
        print(f"Sunt {nr_angajati} persoane in firma cu vechime mai mare de {input_user//365} ani.")
        print("".center(100, '='))
        return informatii_firma()
    elif optiune == '4':
        return None
    else:
        print("    EROARE! Optiunea nu exista.    ".center(100, '#'))
        return informatii_firma()


def adaugare_angajati():
    """
    Functie care corespunde optiunii 3 din meniul principal. Functia ia ca input toate caracteristicile
    unui obiect de tip angajat si il adauga atat in lista din clasa Angajat, cat si in fisierul
    angajat in formatul "departament/nume/functie/data/salar". Exemplu:

        Introduceti departamentul: curatenie
        !!! Departament inexistent !!! Mai incercati o data.
        Introduceti departamentul: HR
        Introduceti numele angajatului: Ion Doe
        Introduceti functia: manager
        Introduceti data angajarii in formatul aaaa-l-zz: 2021-11-22
        Introduceti salariul: 2300t
        Format incorect.
        Introduceti salariul: 3400
        Angajat adaugat cu succes.

    """
    print("    Adaugare angajati    ".center(100, '='))
    Departament.afisare_departamente()
    nume_dep = verificare_denumire(input("Departament: "))
    if nume_dep.upper() not in [departament.nume_dep.upper() for departament in Departament.departamente]:
        print("    EROARE! Departament inexistent.    ".center(100, '#'))
        return adaugare_angajati()
    nume_angajat = verificare_nume(input("Nume: "))
    post = verificare_denumire(input("Functie: "))
    data_angajarii = verificare_data(input("Data angajarii: "))
    salar = verificare_salar(input("Salar: "))
    Angajat.adaugare_angajat(nume_dep, nume_angajat, post, data_angajarii, salar)
    print("    Angajat adaugat cu succes!    ".center(100, '*'))


def iesire():
    """ Functie care corespunde optiunii 4 din meniu. Foloseste functia exit() din modulul sys
    pentru a iesi din program"""

    print("    La revedere!    ".center(100, '='))
    sys.exit()


""" Dictionar care mapeaza fiecare optiune valida din meniul principal cu functia aferenta."""
dict_optiuni = {

    "1": vizualizare,
    "2": informatii_firma,
    "3": adaugare_angajati,
    "4": iesire
}

if __name__ == "__main__":
    # Apelarea functiei load_angajati pentru a incarca datele din fisier in baza curenta de date
    Angajat.load_angajati()
    # Am mutat aici functia pt. ca adauga in continuu ultima versiune a fisierului si se duplicau datele
    while True:
        print("    Inc.    ".center(100, '='))
        print("    1. Vizualizare angajati    ".center(100))
        print("    2. Informatii despre firma    ".center(102))
        print("    3. Adaugare angajati    ".center(95))
        print("    4. Iesire    ".center(85))
        print("".center(100, '='))
        optiune = input("Introduceti optiunea: ")

        # Apelarea optiunii corespunzatoare input-ului
        if optiune in dict_optiuni:
            dict_optiuni[optiune]()
        else:
            print("    EROARE! Optiunea nu exista.    ".center(100, '#'))
            continue
