import math
import os, sys

y_koordinata = float(input ("Y koordinata : "))
x_koordinata = float(input ("X koordinata : "))
tavolsag = float(input ("Tavolsag : "))
fok = int(input("Fok: "))
perc = int(input("Perc: "))
masod = int(input("Masodperc: "))
    
if ((fok < 360) or (perc < 60) or (masod < 60)):
    os.system("cls")

    szog = fok + (perc/60) + (masod/3600)
    V = szog/360*2*math.pi
        
    y_vegleges = round(y_koordinata+tavolsag*math.sin(V),2)
    x_vegleges = round(x_koordinata+tavolsag*math.cos(V),2)

        
    print ("Y = ",y_vegleges) 
    print ("X = ",x_vegleges)
