# -*- coding: utf-8 -*-
import random

#1
def estraiNumero():
    numero = random.randint(5, 20)
    return numero
            
            
numeroEstratto = estraiNumero()
print("Il numero estratto è: ", numeroEstratto)


#2
def numeroMax(primoNumero, secondoNumero):
    if(primoNumero > secondoNumero):
        print("Il numero maggiore è: ", primoNumero)
    else:
        print("Il numero maggiore è: ", secondoNumero)
        
numeroMax(9,7)
numeroMax(2,7)


#8
def reverseString(stringa):
    lunghezzaStringa = len(stringa)-1
    nuovaStringa = ""
    for lettera in stringa:
        nuovaStringa += stringa[lunghezzaStringa]
        lunghezzaStringa -= 1
    return nuovaStringa


reverse = reverseString("cane")
print(reverse)


#7
def pariDispari():
    print("Inserisci un numero:")
    numeroInserito = int(input())
    print(7%2)
    if (numeroInserito % 2) == 0:
        print("Il numero inserito è pari.")
    else:
        print("Il numero inserito è dispari.")
        
pariDispari()



#4 - 5
stringaGlobale = "ppppp ttt"


def contaVocali():
    contatoreVocali = 0
    vocali = "aeiou"
    for lettera in stringaGlobale:
        if lettera in vocali:
            contatoreVocali += 1
    return contatoreVocali

numeroVocali = contaVocali()
print("Il numero di vocali nella frase \'" + stringaGlobale + "\' è: ", numeroVocali)



#6
def contaConsonanti():
    contatoreConsonanti = 0
    vocali = "aeiou "
    for lettera in stringaGlobale:
        if lettera not in vocali:
            contatoreConsonanti += 1
    return contatoreConsonanti

numeroConsonanti = contaConsonanti()
print("Il numero di consonanti nella frase \'" + stringaGlobale + "\' è: ", numeroConsonanti)


#9

def eliminaSpazi (stringa):
    nuovaStringa = ""
    for lettera in stringa:
        if lettera != " ":
            nuovaStringa += lettera
    return nuovaStringa

senzaSpazi = eliminaSpazi(stringaGlobale)
print(senzaSpazi)


#3

def numeriInRange(minimo, massimo):
    contatore = massimo - minimo
    while contatore != 0:
        print(contatore)
        contatore -= 17

numeriInRange(5, 10)