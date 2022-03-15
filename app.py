import numpy as np

def hex_dec(h):
    rest = h[-1]
    mult = h[0]
    if "A"<=rest<="F" :
        rest = ord(rest) - 55
    if "A"<=mult<="F" :
        mult = ord(mult) - 55
    return (16*int(mult))+int(rest)

def rempilre(T):
    F = open("ImgHexa.txt","r")
    line = F.readline()
    i = 0
    while not line == "" :
        T[i]['Hex1'] = line[:len(line)-1]
        T[i]['Num'] = i
        T[i]['Dec1'] = hex_dec(line[:len(line)-1])
        i+=1
        line = F.readline()
    F.close()
    return T,i

def trier(T,i):
    echange = True
    counter =0
    while echange or counter < i:
        echange = False
        for x in range(0,i-1):
            if int(T[x]['Dec1']) >int(T[x+1]['Dec1'])  :
                T[x] ,T[x+1] = T[x+1] ,T[x]
                echange = True
        counter+=1

def genere(nb):
    mot=""
    while not( nb == 0 ):
        r = nb % 3
        if r == 0:
            y="Ma"
        elif r == 1:
            y="Des"
        else:
            y="Son"
        mot = y+mot
        nb = nb // 3
    return mot

def remplire2(T,i):
    F = open("resultat.txt","w")
    for x in range(i):
        text = genere(T[x]["Dec1"]) +" "+ str(T[x]["Num"]) +"\n"
        F.write(text)
    F.close()

#PP

T = np.array([{} for i in range(100)])
T,i = rempilre(T)
trier(T,i)
remplire2(T,i)
    

