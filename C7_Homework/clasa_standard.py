from functii_verificare import *


class Standard:
    lista_utilizatori = []  # lista cu toti utilizatorii, standard si premium

    def __init__(self, nume: str, prenume: str, telefon: str):
        self.nume = nume
        self.prenume = prenume
        self.__telefon = telefon
        self.assets = {'USD': 100, 'EUR': 100, 'BTC': 100}

    def nr_cont(self):  # returneaza numarul de telefon (acesta fiind private)
        return self.__telefon

    @classmethod
    def signup(cls):    # utilizata de oricine pt. a crea un cont
        print("  Sign up  ".center(50, "="))
        nume = verificare_litere(input("Nume: "))
        prenume = verificare_litere(input("Prenume: "))
        telefon = verificare_telefon(input("Telefon: "))
        for i in cls.lista_utilizatori:
            if telefon == i.nr_cont():
                print('  EROARE! Numarul exista deja.  '.center(50, "#"))
                if verificare_optiune(input("Doriti sa mai incercati? (y/n): ")) == 'y':
                    return cls.signup()
                else:
                    return None
        cls.lista_utilizatori.append(cls(nume, prenume, telefon))
        print("   Cont activat cu succes!   ".center(50, "="))

    @classmethod
    def login(cls):    # returneaza "profilul" utilizatorului
        print("  Login  ".center(50, "="))
        telefon = verificare_telefon(input("Telefon: "))
        for i in cls.lista_utilizatori:
            if telefon == i.nr_cont():
                return i
        print('  EROARE! Numarul nu exista.  '.center(50, "#"))
        if verificare_optiune(input("Doriti sa mai incercati? (y/n): ")) == 'y':
            return cls.login()

    def afisare(self):  # utilizata de oricine pt. a-si vedea profilul
        print(f"    {self.prenume}'s profile    ".center(50, "="))
        print("Nume: ", self.nume)
        print("Prenume: ", self.prenume)
        print("Telefon: ", self.nr_cont())
        print("Assets: ", end=" ")
        for i in self.assets:
            print(self.assets[i], i)
            print("        ", end=" ")
        print()
        print("".center(50, "*"))

    def adauga_bani(self):  # utilizata de oricine pt. a adauga bani in cont
        print("  Top-Up  ".center(50, "="))
        print("Sold curent: ", end=" ")
        for j in self.assets:
            print(self.assets[j], j)
            print("             ", end=" ")
        print()
        moneda = verificare_moneda(input("Moneda (USD/EUR/BTC): "))
        suma = verificare_float(input("Suma: "))
        self.assets[moneda] = self.assets[moneda] + suma
        print(f"   Sold nou: {self.assets[moneda]} {moneda}   ".center(50, "-"))
        print("   Banii au intrat in contul Pay!   ".center(50, "$"))

    def cheltuie(self):    # utilizata de oricine pt. a face o plata
        print("  Marketplace  ".center(50, "="))
        print("Sold curent: ", end=" ")
        for j in self.assets:
            print(self.assets[j], j)
            print("             ", end=" ")
        print()
        moneda = verificare_moneda(input("Moneda (USD/EUR/BTC): "))
        suma = verificare_float(input("Suma: "))
        if suma > self.assets[moneda]:
            print('  EROARE! Nu ai destui bani in cont.  '.center(50, "#"))
            if verificare_optiune(input("Doriti sa mai incercati? (y/n): ")) == 'y':
                return self.cheltuie()
            else:
                return None
        self.assets[moneda] = self.assets[moneda] - suma
        print(f"   Sold nou: {self.assets[moneda]} {moneda}   ".center(50, "-"))
        print("   Plata a avut loc cu succes!   ".center(50, "$"))
