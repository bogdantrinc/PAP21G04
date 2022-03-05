class Departament:
    departamente = []

    def __init__(self, nume_dep: str):
        self.nume_dep = nume_dep
        # Departament.departamente.append(self.nume_dep)    # Am putea adauga in lista direct in constructor

    @classmethod
    def afisare_departamente(cls):
        """Metoda de afisare a departamentelor. Exemplu:

        ==== Departamente ====
        - HR
        - IT
        """
        print("Departamentele actuale sunt: ")
        for departament in cls.departamente:
            print(f"     -- {departament.nume_dep}")
