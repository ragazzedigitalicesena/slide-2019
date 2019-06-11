import time
import random


def printIntro():
    print('''Ti trovi in una terra piena di draghi.
Di fronte a te ci sono due grotte
In una grotta si trova un drago simpatico e socievole che
condividerà con te il suo tesoro.
Nell\'altra grotta c\'e invece un drago affamato e vorace.
Dentro quale grotta vuoi entrare? (1 o 2)''')

def playerChoice():
    choice = input()
    return choice

def printChoice(choice):
    print('''Entri dentro la caverna '''+choice+'''
E' buia e spaventosa
Un enorme drago compare all'improvviso davanti a te! Apre
le sue fauci e...''')

def check(answerP, friendlyC):
    if int(answerP) == friendlyC :
           # "1" == 1 ---> FALSE   int(answerP) == friendlyC
        print("'Hai vinto il tesoro!")
    else:
        print("Il drago ti mangia in un boccone!")



printIntro()
answer = playerChoice()
printChoice( answer )
time.sleep(2)

friendlyCave = random.randint(1,2)
check(answer, friendlyCave)

