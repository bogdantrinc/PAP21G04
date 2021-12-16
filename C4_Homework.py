"""
1. Creati un script care sa calculeze valoarea lui x = 3x^2 - 4y + 4 in intervalul 10,20,
   unde y = 3x.
   Creati o functie pentru calcularea lui x si y.

	Sample output:
    ============= X = 10 ==================
    Rezultatul functiei:  184
    ============= X = 11 ==================
    Rezultatul functiei:  235
    ============= X = 12 ==================
    Rezultatul functiei:  292
    ============= X = 13 ==================
    Rezultatul functiei:  355
    ...
"""
# todo

"""
2. Creati un script care cere input de la utilizator cu numarul de carti pe care doreste 
   sa il adauge in biblioteca. 
   Pentru fiecare carte pe care utilizatorul doreste sa o adauge, cere input cu numele 
   cartii, autorul acesteia si anul publicarii. Creati cate un dictionar pentru fiecare carte 
   si creati o lista care sa contina aceste dictionare. Afisati dictionarele.

    Sample output: 
	======== Cartea 1 =========
	Cati carti doriti sa adaugati la lista? 2
    Numele cartii: Inteligenta materiei
    Numele autorului: Constantin Dulcan
    Anul publicarii: 1992
    ======== Cartea 2 =========
    Numele cartii: Cosmos
    Numele autorului: Carl Sagan
    Anul publicarii:1980
    
    Cartile dvs sunt: 
    {'nume': 'Inteligenta materiei', 'autor': 'Constantin Dulcan', 'an': '1992'}
    {'nume': 'Cosmos', 'autor': 'Carl Sagan', 'an': '1980'}
    
    Process finished with exit code 0
"""
nr = input("Cati carti doriti sa adaugati in biblioteca?")
lista_carti = []
for i in range(int(nr)):
   #  todo
   pass

print(lista_carti)

"""
3. Completati sciptul exercitiului anterior in felul urmator:
      - Cereti input de la utilizator cu un an de publicatie si afisati toate cartile 
        aparute dupa anul respectiv

	Sample output:
	Cartile dvs sunt: 
    {'nume': 'Inteligenta materiei', 'autor': 'Constantin Dulcan', 'an': '1992'}
    {'nume': 'Cosmos', 'autor': 'Carl Sagan', 'an': '1980'}
    Anul: 1990
    Inteligenta materiei a fost publicat dupa 1990.
    
    Process finished with exit code 0
"""
# todo