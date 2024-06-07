# Abbiamo 25 studenti; memorizzare questo dato in una variabile.
'''studenti = 25'''
'''print(studenti)'''

# Abbiamo 25 studenti; memorizzare questo dato in una variabile. Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile.
'''studenti = 25
nuovi_studenti = 3
studenti = studenti + nuovi_studenti
print (studenti)'''

'''studenti = 25
nuovi_studenti = 3
studenti += 3
print (studenti)'''

# Creare una variabile che contiene la stringa "Epicode", quindi stamparla a video.
'''x = str("Epicode")
print(x)'''

# Abbiamo la variabile, Incrementarla di 2 e poi moltiplicarla per 3 Usare due metodi diversi (ad esempio, uno utilizzando gli operatori di assegnazione, e uno senza).
'''x = 10
x += 2
x *= 3
print(x)'''

'''x = 10
x = (10 + 2) * 3
print(x)'''

'''numero = int(input ("inserisci: "))
numero += 2
numero *= 3
print(numero)'''

# Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è compreso tra 5 e 8.
'''parola_1 = "Windows"
if len(parola_1) > 5 and len(parola_1) < 8:
    print(True)
else:
    print(False)'''

'''parola_2 = "Excel"
if len(parola_2) > 5 and len(parola_2) < 8:
    print(True)
else:
    print(False)'''

'''parola_3 = "Excel"
if len(parola_3) > 5 and len(parola_3) < 8:
    print(True)
else:
    print(False)'''

'''parola_4 = "Powerpoint"
if len(parola_4) > 5 and len(parola_4) < 8:
    print(True)
else:
    print(False)'''

'''parola_5 = "Word"
if len(parola_5) > 5 and len(parola_5) < 8:
    print(True)
else:
    print(False)'''

# Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è compreso tra 5 e 8.
# Utilizzo funzione "Input".
'''parola = input ("inserisci: ")
if len(parola) > 5 and len(parola) < 8:
    print(True)
else:
    print(False)'''

# Calcolare e stampare a video quanti secondi ci sono in un anno non bisestile.
'''secondi = 366*24*60*60
print(secondi)'''

'''giorni = 366
secondi = giorni*24*60*60
print(secondi)'''

# Calcolare e stampare a video quanti secondi ci sono in un anno non bisestile.
# Funzioni (Es.: formula)
'''def calcola_secondi():
    giorni = int(input("Scrivi il numero di giorni: "))
    secondi = giorni*24*60*60
    if secondi == 31622400:
        print('Anno bisestile: secondi', secondi)
    elif secondi == 31536000:
        print('Anno non bisestile: secondi', secondi)
    elif secondi > 31622400:
        print('Hai inserito un numero di giorni maggiore a 365: secondi', secondi)
    elif secondi < 31622400:
        print ('Hai inserito un numero di giorni inferiore a 365: secondi', secondi)
        calcola_secondi()'''
# Lancio funzione (Es.: utilizzo della formula)
'''calcola_secondi()'''

# Funzione (all'interno ci sono i parametri formali)
'''def calcolatrice(Num1, Num2, Operatore):
    if Operatore == '+':
        return(Num1 + Num2)
    elif Operatore == '-':
        return(Num1 - Num2)
    elif Operatore == '*':
        return(Num1 * Num2)
    elif Operatore == '/':
        return(Num1 / Num2)
    else:
        return 'Operatore non valido'
risultato = calcolatrice(5, 3, '%')
print(risultato)'''

# Abbiamo la seguente stringa: my_string = "I am studying Python" 
#Trasformarla in modo che tutti i caratteri siano maiuscoli (uppercase)
'''frase1 = my_string.upper()
print(frase1)'''
# Trasformarla in modo che tutti i caratteri siano minuscoli (lowercase)
'''frase2 = my_string.lower()
print(frase2)'''
# Sostituire la sottostringa "Python" con la stringa "a lot" 
'''my_string = "I am studying Python"
frase3 = my_string.replace("Python", "a lot")
print(frase3)'''
# Usare il metodo .strip(); cambia qualcosa? Perché?
'''my_string = "I am studying Python"
frase4 = my_string.strip()
print(frase4)'''

'''testo = "Questo è un esempio di split"
suddiviso = testo.split()
print(suddiviso)'''

'''testo = "dividere la stringa in sottostringhe"
diviso = testo.split()
print(diviso)'''

'''parola = "dividere una stringa, in più sottostringhe"
parola.split(",")
print(parola.split(","))'''

'''parola = "dividere una stringa, in più sottostringhe"
diviso = parola.split(",")
print(diviso)'''

'''parola = "dividere una stringa, in più sottostringhe"
diviso = parola.split(",")
print(diviso)'''
'''parole = "aggiungo cose a caso"
print(parola+" "+parole)
print("-"*100)'''

'''x = 12
y = 13
def somma(x, y):
    return x + y
risultato = somma(x, y)
print(risultato)'''

'''def calcolatrice():
    Num1 = int(input("Inserisci il primo numero: "))
    Num2 = int(input("Inserisci il secondo numero: "))
    Operatore = input("Inserisci operatore: ")
    if Operatore == '+':
        print(Num1 + Num2)
    elif Operatore == '-':
        print(Num1 - Num2)
    elif Operatore == '*':
        print(Num1 * Num2)
    elif Operatore == '/':
        print(Num1 / Num2)
    else:
        print('Operatore non valido')
calcolatrice()'''

# Concatenazione stringa + numero (format): mettere "f" all'inizio della stringa.
'''y=3
print(f'Ciao ho {y} anni ')'''

