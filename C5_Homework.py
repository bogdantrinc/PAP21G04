"""
1. Se cere un script care sa simuleze o tombola. Utilizatorul își va adăuga CNP-ul și valoarea
   bonului de cumparaturi. Dacă introduce un CNP valid și are peste 18 ani, va trece mai departe,
   daca nu, se va afișa un mesaj de eroare și programul se va încheia.

    - Dacă valoarea bonului de cumparaturi este mai mica de 100 lei, castigurile sunt:
        Un suc, o punga de chipsuri, o caserola de prajituri
    - Dacă valoarea bonului este între 100 si 500 lei, castigurile sunt:
        Un prajitor de paine, O consola de Gaming, o Tastatura mecanica
    - Dacă valoarea bonului este peste 500 lei, castigurile sunt:
        Un robot de bucatarie, o masina, orice produs de la valorile de castig mai mici.

    *** Calcularea varstei se va face într-o funcție separată
	** Castigul se va extrage cu ajutorul funcției choice() din modulul random
"""
# from datetime import date
# from random import choice
#
#
# def verificare_varsta(valoare):
#     data_nasterii = date.today()
#     if valoare.isdigit() is False and len(valoare) != 13:
#         print("CNP invalid!")
#         return None
#     if valoare[0] in '12':
#         data_nasterii = date(int('19' + valoare[1:3]), int(valoare[3:5]), int(valoare[5:7]))
#     elif valoare[0] in '56':
#         data_nasterii = date(int('20' + valoare[1:3]), int(valoare[3:5]), int(valoare[5:7]))
#     else:
#         return None
#     if (date.today() - data_nasterii).days < 6575:  # 18 years = 6574.35 days
#         print("Esti minor, nu poti participa la loterie!")
#         return None
#     return data_nasterii
#
#
# def cod_numeric(cnp: str, suma: str):
#     castiguri = ["un suc", "o punga de chipsuri", "o caserola de prajituri", "un prajitor de paine", "o consola de Gaming", "o tastatura mecanica", "un robot de bucatarie", "o masina"]
#     varsta = verificare_varsta(cnp)
#     if varsta is None:
#         return None
#     try:
#         suma = float(suma)
#     except BaseException:
#         print("EROARE!, Format incorect.")
#         return None
#     if suma < 100:
#         return " Ai castigat, " + choice(castiguri[:3]) + '! '
#     elif suma < 500:
#         return " Ai castigat, " + choice(castiguri[3:6]) + '! '
#     elif suma > 500:
#         return " Ai castigat, " + choice(castiguri) + '! '
#
#
# print("    Loteria Bonurilor    ".center(50, '='))
# print(str(cod_numeric(input("CNP: "), input("Suma: "))).center(50, '-'))
# print("    La revedere!    ".center(50, '='))

"""
2. Detectati posibilele erori din codul de mai jos care pot apărea în momentul rulării 
   programului și tratati-le folosind excepții.
"""

lst = []
while True:
   numar = input("Introduceti un numar (cand v-ati saturat, apasati q): ")
   if numar == 'q':
       break
   try:
       numar = int(numar)
   except ValueError:
       print("EROARE! Introduceti doar numere intregi.")
   else:
       lst.append(numar)

# Suma numarului de pe pozitia 1 si 2.
print("O sa adaugam numarul 2 si 3.")
try:
    suma = lst[1] + lst[2]
except IndexError:
    print("Nu exista numere pe toate pozitiile alese.")
else:
    print("lst[1] + lst[2] = ", suma)

# Divizia primelor 2 numere din lista
print("Divizia primelor 2 numere din lista este: ")
try:
    diviziune = round(lst[0] / lst[1], 2)
except IndexError:
    print("Nu exista numere pe toate pozitiile alese.")
except ZeroDivisionError:
    print("Nu se poate imparti cu 0.")
else:
    print("lst[0] / lst[1] = ", diviziune)

# Suma tuturor numerelor din lista
sum = 0
for i in lst:
    sum += i
print("Suma tuturor numerelor din lista este: ", sum)
