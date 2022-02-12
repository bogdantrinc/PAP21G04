from clasa_standard import *


class Premium(Standard):

    def __init__(self, nume, prenume, telefon):
        Standard.__init__(self, nume, prenume, telefon)
        self.transferuri = []

    @classmethod
    def transferuri(cls, user):
        # utilizata de contul premium
        # Dupa ce "te loghezi" cu telefonul, transferi bani unui alt numar de telefon
        # transferuri e o lista care retine istoricul transferurilor
        if type(user) is not Premium:
            print('  EROARE! Contul nu este Pay Premium.  '.center(50, "#"))
            return None
        print("  Pay Transfer  ".center(50, "="))
        print("  Transfer instant oriunde in lume.  ".center(50, "-"))
        print("Sold curent: ", end=" ")
        for i in user.assets:
            print(user.assets[i], i)
            print("             ", end=" ")
        print()
        telefon = verificare_telefon(input("Telefon: "))
        for i in cls.lista_utilizatori:
            if telefon == i.nr_cont() and user.nr_cont() != i.nr_cont():
                moneda = verificare_moneda(input("Moneda (USD/EUR/BTC): "))
                suma = verificare_float(input("Suma: "))
                if suma > user.assets[moneda]:
                    print('  EROARE! Nu ai destui bani in cont.  '.center(50, "#"))
                    if verificare_optiune(input("Doriti sa mai incercati? (y/n): ")) == 'y':
                        return cls.transferuri(user)
                    else:
                        return None
                user.assets[moneda] = user.assets[moneda] - suma
                i.assets[moneda] = i.assets[moneda] + suma
                user.transferuri.append(f"{user.nume} {user.prenume} ({user.nr_cont()}) a transferat {suma} {moneda} lui {i.nume} {i.prenume} ({i.nr_cont()})")
                print(f"   Sold nou: {user.assets[moneda]} {moneda}   ".center(50, "-"))
                print(f"  Ai transferat {suma} {moneda} lui {i.nume} {i.prenume}!  ".center(50, "$"))
                return None
        print('  EROARE! Numarul nu exista.  '.center(50, "#"))

    @classmethod
    def afisare_banca(cls):
        # utilizata doar de angajatii bancii
        print("    INFORMATII CONFIDENTIALE    ".center(50, "*"))
        for i in cls.lista_utilizatori:
            if type(i) is Premium:
                print("    Premium    ".center(50, "-"))
            else:
                print("    Standard    ".center(50, "-"))
            print()
            print("Nume: ", i.nume)
            print("Prenume: ", i.prenume)
            print("Telefon: ", i.nr_cont())
            print("Assets: ", end=" ")
            for j in i.assets:
                print(i.assets[j], j)
                print("        ", end=" ")
            print()
            if type(i) is Premium:
                print("Transferuri: ")
                for k in i.transferuri:
                    print(k)
        print("".center(50, "-"))
        print(" ACCESUL INTERZIS! ".center(50, "*"))
