"""
1. Declarați o listă care conține următoarele elemente: [‘abc’,123,’1’,1].
    - afișarea tipului fiecărui element din lista
    - Aflarea numărului numerelor întregi, numerelor float, respectiv a șirurilor din lista
"""
lista = ['abc', 123, '1', 1]
print(f"{lista[0]}: ", type(lista[0]), f"\n{lista[1]}: ", type(lista[1]), f"\n{lista[2]}: ", type(lista[2]), f"\n{lista[3]}: ", type(lista[3]))
nr_int = 0
nr_float = 0
string = 0
for i in lista:
    if str(type(i)) == "<class 'int'>":
        nr_int += 1
    if str(type(i)) == "<class 'str'>":
        string += 1
    if str(type(i)) == "<class 'float'>":
        nr_float += 1
print(f"{nr_int} numere intregi.")
print(f"{string} siruri.")
print(f"{nr_float} numere de tip float.")

"""
2. Luati ca input un sir de la utilizator. Transformați șirul într-o lista și 
   numarati vocalele din aceasta. Afisati numarul vocalelor pe consola.

    Introduceti un cuvant: Ananas
    Vocale in cuvantul dvs: 3
"""
sir = list(input("Sir: ").lower())
counter = 0
for i in sir:
    if i in 'aeiou':
        counter += 1
print("Numarul vocalelor: ", counter)

"""
3. Se cere un script pentru noii vecini într-un cartier. Scriptul:
   - Cere input cu ce provider de Internet dorește utilizatorul. Providerii disponibili sunt: 
     A-Mobile, S5Net, TeleNet. Dacă opțiunea utilizatorului nu se afla in lista, 
     afișați “Utilizatorul nu este disponibil, va rog să alegeți altul.

   - Dupa ce utilizatorul a ales un provider valid, se cere tipul de abonament dorit. 
     Optiunile valide sunt: 500Mbit/s, 1Gb/s, 350Mb/s. Daca utilizatorul nu introduce o optiune 
     valida, se cere din nou pana cand acesta alege una valida.
   
   - La final se afiseaza mesajul: “Cererea a fost inregistrata. Va multumim.”
"""
print("Providerii disponibili sunt: A-Mobile, S5Net, TeleNet.")
while True:
    provider = input("Provider de Internet: ")
    if provider in ["A-Mobile", "S5Net", "TeleNet"]:
        break
    print("Utilizatorul nu este disponibil, va rog să alegeți altul.")
print("Abonamentele disponibile sunt: 500Mbit/s, 1Gb/s, 350Mb/s.")
while True:
    abonament = input("Tipul de abonament dorit:")
    if abonament in ["500Mbit/s", "1Gb/s", "350Mb/s"]:
        break
    print("Abonamentul nu este disponibil, va rog să alegeți altul.")
print("Cererea a fost inregistrata. Va multumim.")
