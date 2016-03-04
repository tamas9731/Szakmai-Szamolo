import math
import os, sys

Ay = float(input("A pont Y koordinata : "))
Ax = float(input("A pont X koordinata : "))

By = float(input("B pont Y koordinata : "))
Bx = float(input("B pont X koordinata : "))

tAP = float( input("AP tavolsag : "))
tBP = float( input("BP tavolsag : "))

ky = Allaspont_YA = Ay 
kx = Allaspont_XA = Ax
vy = Allaspont_YB = By
vx = Allaspont_XB = Bx

#Irányszög A-B

ABszogu=math.degrees(math.atan((Allaspont_YB-Allaspont_YA)/(Allaspont_XB-Allaspont_XA)))
    
if ((vy-ky)>0) and ((vx-kx)>0):
    ABszogo=ABszogu
elif ((vy-ky)>0) and ((vx-kx)<0):
    ABszogo=ABszogu+180
elif ((vy-ky)<0) and ((vx-kx)<0):
    ABszogo=ABszogu+180
elif ((vy-ky)<0) and ((vx-kx)>0):
    ABszogo=ABszogu+360
   
ABszogd=int(ABszogo)
ABszogm=int((ABszogo-int(ABszogd))*60)
ABszogs=int(round((((ABszogo-ABszogd)*60)-ABszogm)*60))

wszog = math.degrees(ABszogd + (ABszogm/60) + (ABszogs/3600))
ABszog = wszog/360*2*math.pi

tAB = round(math.sqrt(((Allaspont_YB-Allaspont_YA)**2)+((Allaspont_XB-Allaspont_XA)**2)),2)

if (ABszog > 180):
    BAszog = ABszog - 180
else:
    BAszog = ABszog + 180

Alfaszog = math.degrees(math.acos((tAB**2 + tAP**2 - tBP**2)/(2*tAB*tAP)))
Betaszog = math.degrees(math.acos((tBP**2 + tAB**2 - tAP**2)/(2*tBP*tAB)))
Gammaszog = math.degrees(math.acos((tAP**2 + tBP**2 - tAB**2)/(2*tAP*tBP)))

if (ABszog < 180):
    APszog = ABszog - Alfaszog
else:
    APszog = ABszog + Alfaszog

if (BAszog < 180):
    BPszog = BAszog - Betaszog
else:
    BPszog = BAszog + Betaszog

sinaps = math.sin(math.radians(APszog))
cosaps = math.cos(math.radians(APszog))

sinabs = math.sin(math.radians(BPszog))
cosabs = math.cos(math.radians(BPszog))

Ayv = round(ky+tAP*sinaps,2)
Axv = round(kx+tAP*cosaps,2)

Byv = round(vy+tBP*sinabs,2)
Bxv = round(vx+tBP*cosabs,2)

y = (Ayv+Byv)/2
x = (Axv+Bxv)/2

print("tAP : ",tAP)
print("tBP : ",tBP)
print("tAB : ",tAB)
print("APszog : ",APszog)
print("BPszog : ",BPszog )
print("ABszog : ",ABszog)
print("BAszog : ",BAszog)
print("Alfaszog : ",Alfaszog)
print("Betaszog : ",Betaszog)
print("Gammaszog : ",Gammaszog)
print("Sin AP : ",sinaps)
print("Cos AP : ",cosaps)
print("Sin BP : ",sinabs)
print("Cos BP : ",cosabs)
print(y)
print(x)
