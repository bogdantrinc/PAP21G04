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
# todo

"""
2. Detectati posibilele erori din codul de mai jos care pot apărea în momentul rulării 
   programului și tratati-le folosind excepții.
"""

lst = []
while True:
   numar = input("Introduceti un numar (cand v-ati saturat, apasati q): ")
   if numar == 'q':
       break
   numar = int(numar)
   lst.append(numar)

# Suma numarului de pe pozitia 1 si 2.
print("O sa adaugam numarul 2 si 3.")
print("lst[1] + lst[2] = ", lst[1] + lst[2])

# Divizia primelor 2 numere din lista
print("Divizia primelor 2 numere din lista este: ")
print("lst[0] / lst[1] = ", lst[0] / lst[1])

# Suma tuturor numerelor din lista
sum = 0
for i in lst:
   sum += i
print("Suma tuturor numerelor din lista este: ", sum)
