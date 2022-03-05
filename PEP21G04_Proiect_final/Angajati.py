import datetime

from Departament import Departament


class Angajat(Departament):
    """
    Clasa care deriva din Departament si reprezinta fiecare obiect de tip Angajat.
    """
    angajati = []

    def __init__(self, nume_dep, nume_angajat: str, post: str, data_angajarii: datetime.date, salar: float):
        """
        :param nume_dep: string (mostenit din clasa Departament)
        :param nume_angajat: string
        :param post: string
        :param data_angajarii: datetime.date()
        :param salar: float
        """
        Departament.__init__(self, nume_dep)
        self.nume_angajat = nume_angajat
        self.post = post
        self.data_angajarii = data_angajarii
        self.salar = salar

    @classmethod
    def load_angajati(cls):
        """
        Metoda de clasa care incarca si creaza obiecte de tip Angajat,
        dupa care le adauga in lista angajati:

        """
        #  -- Deschide fisierul "angajati.txt" si obtine o lista_angajati in formatul:
        #  ["HR/Maria Popescu/Manager/2020-7-12/7600","nume_dep/nume/post/data_angajarii/salar"]
        with open("angajati.txt") as f:
            lista_angajati = f.read().splitlines()

        # Parcurge lista obtinuta mai sus si imparte fiecare element in functie de "/".
        for angajat in lista_angajati:
            #  Se obtine lista ang in formatul:
            #  ["HR","Maria Popescu", "Manager",  "2020-7-12", "7600"]
            ang = angajat.split("/")

            # Converteste data angajarii din string in datetime.date, dandu-i split in functie de "-".
            # data_ang[1] va fi "2020", data_ang[2] va fi "7", data_ang[3] va fi "12"
            data_ang = ang[3].split("-")
            data_ang = datetime.date(int(data_ang[0]), int(data_ang[1]), int(data_ang[2]))

            # Creaza obiectul de tip Angajat cu parametrii dati
            cls.angajati.append(Angajat(ang[0], ang[1], ang[2], data_ang, float(ang[4])))

            # Daca departamentul nu exista, il va adauga in lista de departamente. Fara duplicate.
            if ang[0].upper() not in [i.nume_dep.upper() for i in Departament.departamente]:
                departament = Departament(ang[0])
                Departament.departamente.append(departament)

    @classmethod
    def afisare_angajati(cls):
        """
        Va afisa angajatii in functie de departament, in urmatorul format:
        ========= HR =========
        --------------
        Nume: Maria Popescu
        Functie: Manager
        Data angajarii: 2020-7-12
        Salar: 7600 lei
        ---------------
        Nume: x
        Functie: y
        Data angajarii: xx-x-xx
        Salar: xxxx lei
        ========= IT ==========
        ------------
        Nume: y
        Functie: xx
        ...
        etc.
        """
        for nume_dep in Departament.departamente:
            print(f"    Departament {nume_dep.nume_dep}    ".center(100, '='))
            for angajat in cls.angajati:
                if nume_dep.nume_dep.upper() == angajat.nume_dep.upper():
                    print(f"Nume: {angajat.nume_angajat}")
                    print(f"Functie: {angajat.post}")
                    print(f"Data angajarii: {angajat.data_angajarii}")
                    print(f"Salar: {angajat.salar} Lei")
                    print("".center(100, '-'))

    @classmethod
    def afisare_departament(cls, dep: str):
        """
        Afiseaza angajatii din departamentul dep, dat ca parametru
        """
        if dep.upper() not in [denumire.nume_dep for denumire in Departament.departamente]:
            print("    EROARE! Departament inexistent!    ".center(100, '#'))
            return None
        print(f"    Departament {dep.upper()}    ".center(100, '='))
        for angajat in cls.angajati:
            if angajat.nume_dep.upper() == dep.upper():
                print(f"Nume: {angajat.nume_angajat}")
                print(f"Functie: {angajat.post}")
                print(f"Data angajarii: {angajat.data_angajarii}")
                print(f"Salar: {angajat.salar} Lei")
                print("".center(100, '-'))

    @classmethod
    def adaugare_angajat(cls, nume_dep, nume_angajat, post, data_angajarii, salar):
        """
        Metoda de adaugare a angajatilor in lista de angajati
        * Sugestie: apelati in interiorul acestei metode, metoda de update pentru a face update
        la fisierul angajati.txt cu angajatii adaugati

        """
        angajat = Angajat(nume_dep, nume_angajat, post, data_angajarii, salar)  # retine obiectul angajat nou
        cls.angajati.append(angajat)    # adauga in lista de angajati obiectul
        Angajat.update_fisier()    # actualizeaza lista de angajati

    @classmethod
    def update_fisier(cls):
        """
        Metoda de update a fisierului cu angajatii actuali.
        """
        with open("angajati.txt", 'w') as f:
            for om in cls.angajati:    # parcurge lista de angajati si ii adauga pe rand in fisier pe rand nou
                f.write(f"{om.nume_dep}/{om.nume_angajat}/{om.post}/{om.data_angajarii}/{om.salar}\n")
