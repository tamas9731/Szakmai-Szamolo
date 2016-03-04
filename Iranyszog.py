import math
import os, sys

ky=float(input("Kezdopont Y: "))
kx=float(input("Kezdopont X: "))
vy=float(input("Vegpont Y: "))
vx=float(input("Vegpont X: "))
    
szogu=math.degrees(math.atan((vy-ky)/(vx-kx)))
    
if ((vy-ky)>0) and ((vx-kx)>0):
    szog=szogu
elif ((vy-ky)>0) and ((vx-kx)<0):
    szog=szogu+180
elif ((vy-ky)<0) and ((vx-kx)<0):
    szog=szogu+180
elif ((vy-ky)<0) and ((vx-kx)>0):
    szog=szogu+360
        
szogd=int(szog)
szogm=int((szog-int(szogd))*60)
szogs=int(round((((szog-szogd)*60)-szogm)*60))

os.system("cls")
    
print(szogd,"-",szogm,"-",szogs)
dis=round(math.sqrt(((vy-ky)**2)+((vx-kx)**2)),2)
print (dis,"m")
