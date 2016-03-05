import math
import os, sys

Allaspont_YA = float(input("A pont Y koordinata : "))
Allaspont_XA = float(input("A pont X koordinata : "))

Allaspont_YB = float(input("B pont Y koordinata : "))
Allaspont_XB = float(input("B pont X koordinata : "))

Alfad = float(input("Alfa Fok: "))
Alfam = float(input("Alfa Perc: "))
Alfas = float(input("Alfa Másodperc: "))

Betad = float(input("Beta Fok: "))
Betam = float(input("Beta Perc: "))
Betas = float(input("Beta Másodperc: "))

Alfaaszog = math.degrees(Alfad + (Alfam/60) + (Alfas/3600))
Alfaszog = Alfaaszog/360*2*math.pi

Betaaszog = math.degrees(Betad + (Betam/60) + (Betas/3600))
Betaszog = Betaaszog/360*2*math.pi

Gammaszog = 180-(Alfaszog+Betaszog)

ky = Allaspont_YA
kx = Allaspont_XA
vy = Allaspont_YB
vx = Allaspont_XB

#Irányszög A-B

ABszogu=math.degrees(math.atan((vy-ky)/(vx-kx)))
        
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

tAB = round((math.sqrt(((vy-ky)**2)+((vx-kx)**2))),2)

if (ABszog > 180):
    BAszog = ABszog - 180
else:
    BAszog = ABszog + 180

sinalf = math.sin(math.radians(Alfaszog))
sinbet = math.sin(math.radians(Betaszog))
singam = math.sin(math.radians(Gammaszog))

tAP = (sinbet / singam) * tAB
tBP = (sinalf / singam) * tAB

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

#print("ABszog : ",ABszog)
#print("BAszog : ",BAszog)
#print("Alfaszog : ",Alfaszog)
#print("Betaszog : ",Betaszog)
#print("Gammaszog : ",Gammaszog)
#print("tAB : ",tAB)
#print("tAP : ",tAP)
#print("tBP : ",tBP)
#print("AP szog : ", APszog)
#print("BP szog : ", BPszog)
print(y)
print(x)




