"""
1. Parola unui sistem este: Passme1n. Cereți input de la utilizator cu parola.
Afișați pe ecran un mesaj (True, False) daca aceasta este Passme1n, respectiv dacă nu este aceasta.
"""
print(input("Parola: ") == 'Passme1n')

"""
2. Cereți ca input de la utilizator 2 nume. Verificati si afisati:
    Lungimea primului nume
    Dacă cele doua nume date sunt la fel
    Dacă primul nume este mai lung decat al doilea nume
    Inițiala primului nume
    Primul nume inversat
"""
nume_1 = input("Primul nume: ")
nume_2 = input("Al doilea nume: ")
print("Lungimea primului nume: ", len(nume_1))
print("Cele doua nume date sunt la fel: ", nume_1 == nume_2)
print("Primul nume este mai lung decat al doilea nume: ", len(nume_1) > len(nume_2))
print("Inițiala primului nume: ", nume_1[0])
print("Primul nume inversat: ", nume_1[::-1])

"""
3. Folosind codul de la exercitiul 2, mai cereți input de la utilizator cu un număr:
Afisati primul nume multiplicat de n ori, unde n este numărul introdus de către utilizator.

    Introduceti un nume de referinta: Ana
    Introduceti un alt nume: An
    Lungimea numelui de referinta este:  3
    Numele de referinta este acelasi cu numele dat: False
    Numele de referinta este mai lung decat numele dat: True
    Initiala numelui de referinta este:  A
    Numele de referinta inversat este: anA
    Introduceti un numar: 3
    AnaAnaAna
"""
# nume_1 si nume_2 folosit din exercitiul anterior
numar = input("Numar: ")
print(f"Primul nume multiplicat de {numar} ori: ", nume_1*int(numar))

"""
4. Declarați o variabila cu șirul: “Ananas”. Afișati șirul în următoarele feluri pe ecran:
   -    A
        n
        a
        n
        a
        s
   -    Ana
        nas
   -    An:ana:s
   -    Ana_na_s
   -    nananananananana
"""
variabila = "Ananas"
print(variabila[0], variabila[1], variabila[2], variabila[3], variabila[4], variabila[5], sep='\n')
print(variabila[:3], variabila[-3:], sep='\n')
print(variabila[:2], variabila[2:5], variabila[-1], sep=':')
print(variabila[1:5] * 4)
