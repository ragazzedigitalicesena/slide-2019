# es 2

#Crea una funzione che, dati due parametri in ingresso, restituisca il massimo tra i due. Chiama poi questa funzione
#passandogli due numeri che vuoi tu!

def fa(ea, da):            # o semplicemente return max(ea, da)
    if ea>da:
        return ea
    if da>ea:
        return da
ea=input()
da=input()
eaNum=int(ea)
daNum=int(da)
gg=fa(eaNum, daNum)
print(gg)