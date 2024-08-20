#Liste
'''mia_lista = ["lista", "di", "elementi"]
print(mia_lista)''' 

#Liste (Index)
'''mia_lista = ["lista", "di", "elementi"]
print(mia_lista)
primo_elemento = mia_lista[0]
print(primo_elemento)

mia_lista[0] = "Tien vuole cambiare questo"
print(mia_lista)
print(primo_elemento)

nuova_lista = [[1, 2, 3], [4, 5, 6]]
print(nuova_lista)
nuova_variabile = nuova_lista[0]
print(nuova_variabile)
nuova_variabile.append(5)
print(nuova_variabile)'''

#Liste (Slicing)
'''lista_spesa = ["pomodori", "pasta", "carne", "pesce", "insalata", "biscotti"]
print(lista_spesa)
print(lista_spesa[0:3])
print(lista_spesa[0:4:3])
print(lista_spesa[5:3])'''

#Liste (Append ed Extend)
'''altra_lista = [1, 2, 3, 4, 5, 6, 7, 8,]
bella_lista = [9, 10, 11, 12]
altra_lista.append(bella_lista)
print(altra_lista)
altra_lista.extend(bella_lista)
print(altra_lista)'''

#Liste (Insert)
'''altra_lista = [1, 2, 3, 4, 5, 6, 7, 8]
altra_lista.insert(0, 9)
print(altra_lista)'''

#Liste (Pop)
'''altra_lista = [1, 2, 3, 4, 5, 6, 7, 8]
numero_otto = altra_lista.pop(3)
print(numero_otto)
print(altra_lista)'''

#Liste (Count)
'''pippo_lista = ["a", "b", "b", "c", "c", "c"]
conta_b = pippo_lista.count("b")
print(conta_b)'''

'''pippo_lista = ["a", "b", "b", "b", "c", "c", "c"].count("c")
print(pippo_lista)'''

#Liste (Sort: non si può assegnare ad una variabile)
'''topolino_lista = [3, 2, 10, 5, 1, 8, 6]
topolino_lista.sort()
print(topolino_lista)'''

#Liste (Sort: per assegnare ad una variabile utilizzare "Sorted")
'''topolino_lista = [3, 2, 10, 5, 1, 8, 6]
lista_ordinata = list(sorted(topolino_lista))
print(lista_ordinata)'''

#Liste (Reverse)
'''topolino_lista = [1, 2, 3, 4, 5, 6, 7]
topolino_lista.reverse()
print(topolino_lista)'''

'''topolino_lista = [1, 2, 3, 4, 5, 6, 7]
lista_invertita = list(reversed(topolino_lista))
print(lista_invertita)'''

#Tuple
'''mia_tupla = (1, "ciao", True, ["posso", "mettere", "una", "lista", "in", "una", "tupla"])
print(mia_tupla)'''

#Tuple (Index)
'''mia_tupla = (1, "ciao", True, ["posso", "mettere", "una", "lista", "in", "una", "tupla"])
mio_elemento = mia_tupla[2]
print(primo_elemento)'''

#Tuple (Count)
'''mia_tupla = (1, "ciao", True, ["posso", "mettere", "una", "lista", "in", "una", "tupla"], "ciao")
conta_elemento = mia_tupla.count("ciao")
print(conta_elemento)'''

#Set
'''mio_set = {1, "due", 3, 4, 5, "altra stringa", 3, 4}
print(mio_set)'''

#Set (Add)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_set.add(6)
print(mio_set)'''

#Set (Remove: se lo eseguo una seconda volta mi da errore perchè non trova più l'elemento rimosso)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_set.remove(1)
print(mio_set)'''

#Set (Discard: si può eseguire più volte)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_set.discard(1)
print(mio_set)'''

#Set (Pop: toglie un elemento a caso)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_set.pop()
print(mio_set)'''

#Set (Update)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mia_lista = [1, 2, 3, "bello", "mio"]
mio_set.update(mia_lista)
print(mio_set)'''

#Set (Union)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_secondo_set = {1, 2, 3, "bello", "mio"}
mio_set = mio_set.union(mio_secondo_set)
print(mio_set)'''

#Set (Intersection)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_secondo_set = {1, 2, 3, "bello", "mio"}
mio_set = mio_set.intersection(mio_secondo_set)
print(mio_set)'''

#Set (Difference: mi da elementi che sono contenuti solo nel primo set)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_secondo_set = {1, 2, 3, "bello", "mio"}
mio_set = mio_set.difference(mio_secondo_set)
print(mio_set)'''

#Set (Symmetric_Difference: mi da elementi che sono contenuti solo nel primo set ed elementi contenuti solo nel secondo set)
'''mio_set = {1, "due", 3, 4, 5, "altra stringa"}
mio_secondo_set = {1, 2, 3, "bello", "mio"}
mio_set = mio_set.symmetric_difference(mio_secondo_set)
print(mio_set)'''

#Set (Issubset: mi da True o False a seconda che il secondo Set sia o no un sottinsieme del primo Set)
#False
'''mio_set = {"due", 3, 4, 5, "altra stringa"}
mio_secondo_set = {1, 2, "bello", "mio"}
sottinsieme = mio_secondo_set.issubset(mio_set)
print(sottinsieme)'''
#True
'''mio_set = {1, 2, 3, 4, 5}
mio_secondo_set = {4, 5}
sottinsieme = mio_secondo_set.issubset(mio_set)
print(sottinsieme)'''

#Set (Issuperset: contrario di Issubset)
#False
'''mio_set = {"due", 3, 4, 5, "altra stringa"}
mio_secondo_set = {1, 2, "bello", "mio"}
sottinsieme = mio_set.issuperset(mio_secondo_set)
print(sottinsieme)'''
#True
'''mio_set = {1, 2, 3, 4, 5}
mio_secondo_set = {4, 5}
sottinsieme = mio_set.issuperset(mio_secondo_set)
print(sottinsieme)'''

#Dizionari (Chiave deve essere univoca e immutabile come stringhe tuple o numeri, il valore può essere un dato qualsiasi)
#mio_dizionario = {"chiave": "valore",
#                   "chiave1": "valore1"}
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
print(mio_dizionario)'''

#Dizionari (Indexing: si fa utilizzando la chiave)
#Indexin(1)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
print(mio_dizionario["Nome"])'''
#Indexing(2)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
mio_dizionario["Professione"] = "Data Analyst"
print(mio_dizionario)'''

#Dizionari (Get)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
chiave = mio_dizionario.get("Nome")
print(chiave)'''

#Dizionari (Items)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
miei_elementi = mio_dizionario.items()
print(miei_elementi)'''

#Dizionari (Keys)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
mie_chiavi = mio_dizionario.keys()
print(mie_chiavi)'''

#Dizionari (Values)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
miei_valori = mio_dizionario.values()
print(miei_valori)'''

#Dizionario (Pop: elimina Valore associato alla Chiave specificata)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
mio_pop = mio_dizionario.pop("Nome")
print(mio_pop)
print(mio_dizionario)'''

#Dizionario (Popitem: elimina coppia Chiave/Valore a caso)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
mio_popitem = mio_dizionario.popitem()
print(mio_popitem)
print(mio_dizionario)'''

#Dizionario (Update)
'''mio_dizionario = {"Nome": "Kevin",
                  "Cognome": "Motta",
                  "Età": 29,
                  "Capelli": True}
suo_dizionario = {"Occupazione": "Data Analyst",
                  "Ral": 40000}
mio_dizionario.update(suo_dizionario)
print(mio_dizionario)'''

#If, Elif, Else
#Funzione
'''def numero(eta):
    if eta >= 18 and eta <= 25:
        print("Ammesso")
    elif eta < 18 and eta >= 15:
        print("Troppo giovane")
    elif eta > 25:
        print("Troppo vecchio")
    elif eta < 15:
        print("Eccessivamente giovane")
    else:
        print("Non considerabile")
numero()'''

#Funzione a terminale
'''def numero():
    eta = int(input("Inserisci eta: "))
    if eta >= 18 and eta <= 25:
        print("Ammesso")
    elif eta < 18 and eta >= 15:
        print("Troppo giovane")
    elif eta > 25:
        print("Troppo vecchio")
    elif eta < 15:
        print("Eccessivamente giovane")
    else:
        print("Non considerabile")
numero()'''

#Loop con While e For
#While(1)
'''numero = 0'''
'''while numero <= 10:
    print(numero)
    print("Numero è minore o uguale a 10")
    numero += 1
    print()
    print("Sono uscito dal loop")'''
#While(2)
'''while numero <= 10:
    numero += 1
    print(numero)
    if numero % 2 == 0:
        print("è pari")
    else:
        print("è dispari")
print("Sono uscito dal loop")'''
#For(1)
'''mia_lista = [0, 1, 2, 3, 4]
numeri_pari = []
numeri_dispari = []
for numero in mia_lista[1:4]:
    if numero % 2 == 0:
        numeri_pari.append(numero)
    else:
        numeri_dispari.append(numero) 
print(numeri_pari)
print(numeri_dispari)
print("sono fuori dal loop")'''  

'''mia_stringa = "Ciao sono Kevin, ho 29 anni e vivo a Pavia"
for x in mia_stringa:
    print(x)'''
#For(2: con funzione range)
'''mia_lista = []
for x in range(1, 11):
    mia_lista.append(x+10)
    print(mia_lista)
print(mia_lista)'''
#For(3: con break)
'''mia_lista = ["uno", "due", "tre", "quattro", "cinque"]
indice = []
for num in range(0, len(mia_lista)):
    print(num, mia_lista[num])
    if num == 3:
        break'''