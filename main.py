import numpy as np
import math

#netzwerk=[[],[],[]]

#print(netzwerk)



def knotenerzeugen(n):#erzeugt eine Liste von n Knoten
    knoten=[]
    for i in range(1,n+1):
        knoten.append(i)
    return(knoten)

def kantenerzeugen(knot,n):#erzeugt Kanten für 4 Layer
    kanten=[]
    # Layer 1 hat n Knoten (1 bis n)
    # Layer 2 hat 2n Knoten (n+1 bis 3n)
    # Layer 3 hat 2n Knoten (3n+1 bis 5n)
    # Layer 4 hat n Knoten (5n+1 bis 6n)
    # Jeder Knoten in Layer i ist mit allen Knoten in Layer i+1 verbunden
    if 1<=knot and knot<=n:
        kanten=[j for j in range(n+1,3*n+1)]
        return(kanten)
    if n+1 <= knot and knot <= 3*n:
        vorg=[j for j in range(1,n+1)]
        nachf=[j for j in range(3*n+1,5*n+1)]
        for i in vorg:
            kanten.append(i)
        for i in nachf:
            kanten.append(i)
        return (kanten)
    if 3*n+1 <= knot and knot <= 5*n:
        vorg = [j for j in range(n+1, 3*n+1)]
        nachf = [j for j in range(5*n+1,6*n+1)]
        for i in vorg:
            kanten.append(i)
        for i in nachf:
            kanten.append(i)
        return (kanten)
    if 5*n+1 <= knot or knot<=6*n:
        kanten=[j for j in range(3*n+1,5*n+1)]
        return (kanten)
    return(kanten)

def gewichteinit(kantenliste):#initilisiert alle Kanten mit dem Gewicht 1
    gewichte=[]
    for kanten in kantenliste:
        gewichte.append(1/kanten)
    return(gewichte)

def vorgaenger(knoten,kanten,gewichte):#
    vorg=[]
    vorggewichte=[]
    for i in range(0,len(kanten)):
        if kanten[i]<knoten:
            vorg.append(kanten[i])
            vorggewichte.append(gewichte[i])
    return(vorg,vorggewichte)

def nachfolger(knoten,kanten,gewichte):
    nachf=[]
    nachfgewichte=[]
    for i in range(0,len(kanten)):
        if kanten[i]>knoten:
            nachf.append(kanten[i])
            nachfgewichte.append(gewichte[i])
    return(nachf,nachfgewichte)

def anfangsbelegung(knoten,n):
    if knoten<=int(n/2):
        return(1)
    if knoten >= int(n/2):
        return(0)

def skalarprod(a,b):#berechnet das Skalarprodukt aus a und b. Gibt "false" zurück, wenn die Anzahl der Einträge nicht übereinstimmt
    #print("In Skalarprodukt",a,b)
    if len(a)!=len(b):
        return(false)
    else:
        skp=0
        for i in range(0,len(a)):
            skp=skp+a[i]*b[i]
        return(skp)


def ausgabeberechnen(skp,bias):#berechnet den Ausgabewert 0 oder 1 je nachdem, ob die Sigmoid-Funktion größer als 0,5 ist oder nicht
    x=1/(1+math.exp(-skp-bias))
    if skp>= 0.5:
        return 1
    else:
        return 0

def auswerten(knoten,nachbarn,nachbargewichte,bias):
    #print("Knoten ist",knoten)
    #print("Seine Nachbarn sind:")
    beleg=[]
    for i in nachbarn:
        #print(i)
        #print("Belegung",netzwerk[i][3])
        beleg.append(netzwerk[i][3])
    #print("Nachbarn sind",nachbarn)
    #print("Nachbargewichte sind",nachbargewichte)
    #print("Nachbarbelegung ist",beleg)
    skp=skalarprod(beleg,nachbargewichte)
    wert=ausgabeberechnen(skp,bias)
    return wert

# Netzwerk besteht aus vier Layern
# Layer 1 hat n Knoten
# Layer 1 hat n Knoten
# Layer 3 hat 4n Knoten
# Layer 4 hat n Knoten

n=6

knoten=knotenerzeugen(n+2*n+2*n+n)
belegung=knoten

netzwerk=[]
for i in knoten:
    #print("Knoten",i)
    kanten=kantenerzeugen(i,n)
    #print(kanten)
    gewichte=gewichteinit(kanten)
    wert=anfangsbelegung(i,n)
    netzwerk.append([i,kanten,gewichte,wert])
#print(netzwerk)
#print(netzwerk[1][1][3])
print("Das Netzwerk hat ",n+2*n+2*n+n,"Knoten")
print("Layer 1 hat",n,"Knoten, mit den Nummern",1,"bis ",n)
print("Layer 2 hat", 2*n, "Knoten, mit den Nummern",n+1,"bis ",3*n)
print("Layer 3 hat",2*n,"Knoten, mit den Nummern",3*n+1,"bis ",5*n)
print("Layer 4 hat", n," Knoten, mit den Nummern",5*n+1,"bis ",6*n)
print("Alle Knoten eines Layers sind mit allen Koten der vorherigen und nachfolgenden Layern verbunden")
print("")
bsp=12
print("Ein Beispiel-Knoten:")
print("====================")
print("Knoten-Nummer",netzwerk[bsp][0])
print("Seine Nachbarn:",netzwerk[bsp][1])
print("Die Gewichte der Kanten:",netzwerk[bsp][2])
print("Die Vorgänger-Knoten von",netzwerk[bsp][0],":")
print(vorgaenger(netzwerk[bsp][0],netzwerk[bsp][1],netzwerk[bsp][2]))
print("Die Nachfolger-Knoten von",netzwerk[bsp][0],":")
print(nachfolger(netzwerk[bsp][0],netzwerk[bsp][1],netzwerk[bsp][2]))
print("Der Wert von Knoten",netzwerk[bsp][0]," ist",netzwerk[bsp][3])
[vorg,vorggewichte]=vorgaenger(netzwerk[bsp][0],netzwerk[bsp][1],netzwerk[bsp][2])
print(auswerten(netzwerk[bsp][0],vorgaenger(netzwerk[bsp][0],netzwerk[bsp][1],netzwerk[bsp][2])[0],vorgaenger(netzwerk[bsp][0],netzwerk[bsp][1],netzwerk[bsp][2])[1],2))
#print((netzwerk[5][0],netzwerk[5][1],netzwerk[5][2]))
#print(vorgaenger(netzwerk[5][0],netzwerk[5][1],netzwerk[5][2]))


