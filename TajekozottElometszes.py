import math
import os, sys
print("CSAK KETTO TAJEKOZOIRANY HASZNALHATO EGY PONTON\n")

Ay = ky = float(input("A pont Y koordinata : "))
Ax = kx = float(input("A pont X koordinata : "))

By = vy = float(input("\nB pont Y koordinata : "))
Bx = vx = float(input("B pont X koordinata : "))

Ty1 = float(input("\nA pont 1, Tajekozas Y koordinata : "))
Tx1 = float(input("A pont 1, Tajekozas X koordinata : "))

Ty2 = float(input("\nA pont 2, Tajekozas Y koordinata : "))
Tx2 = float(input("A pont 2, Tajekozas X koordinata : "))

Ty3 = float(input("\nB pont 1, Tajekozas Y koordinata : "))
Tx3 = float(input("B pont 1, Tajekozas X koordinata : "))

Ty4 = float(input("\nB pont 2, Tajekozas Y koordinata : "))
Tx4 = float(input("B pont 2, Tajekozas X koordinata : "))

LAPszogd = int(input("\nAP leolvasas Fok : "))
LAPszogm = int(input("AP leolvasas Perc : "))
LAPszogs = int(input("AP leolvasas Masodperc : "))

Lapszog = math.degrees(LAPszogd + (LAPszogm/60) + (LAPszogs/3600))
LAPszog = Lapszog/360*2*math.pi

LBPszogd = int(input("\nBP leolvasas Fok : "))
LBPszogm = int(input("BP leolvasas Perc : "))
LBPszogs = int(input("BP leolvasas Masodperc : "))

Lbpszog = math.degrees(LBPszogd + (LBPszogm/60) + (LBPszogs/3600))
LBPszog = Lbpszog/360*2*math.pi

LAT1szogd = int(input("\nAT1 leolvasas Fok : "))
LAT1szogm = int(input("AT1 leolvasas Perc : "))
LAT1szogs = int(input("AT1 leolvasas Masodperc : "))

Lat1szog = math.degrees(LAT1szogd + (LAT1szogm/60) + (LAT1szogs/3600))
LAT1szog = Lat1szog/360*2*math.pi

LAT2szogd = int(input("\nAT2 leolvasas Fok : "))
LAT2szogm = int(input("AT2 leolvasas Perc : "))
LAT2szogs = int(input("AT2 leolvasas Masodperc : "))

Lat2szog = math.degrees(LAT2szogd + (LAT2szogm/60) + (LAT2szogs/3600))
LAT2szog = Lat2szog/360*2*math.pi

LBT1szogd = int(input("\nBT1 leolvasas Fok : "))
LBT1szogm = int(input("BT1 leolvasas Perc : "))
LBT1szogs = int(input("BT1 leolvasas Masodperc : "))

Lbt1szog = math.degrees(LBT1szogd + (LBT1szogm/60) + (LBT1szogs/3600))
LBT1szog = Lbt1szog/360*2*math.pi

LBT2szogd = int(input("\nBT2 leolvasas Fok : "))
LBT2szogm = int(input("BT2 leolvasas Perc : "))
LBT2szogs = int(input("BT2 leolvasas Masodperc : "))

Lbt2szog = math.degrees(LBT2szogd + (LBT2szogm/60) + (LBT2szogs/3600))
LBT2szog = Lbt2szog/360*2*math.pi

########################Irányszög A-B####################################

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

########################Irányszög A-T1####################################

AT1szogu=math.degrees(math.atan((Ty1-ky)/(Tx1-kx)))
        
if ((Ty1-ky)>0) and ((Tx1-kx)>0):
    AT1szogo=AT1szogu
elif ((Ty1-ky)>0) and ((Tx1-kx)<0):
    AT1szogo=AT1szogu+180
elif ((Ty1-ky)<0) and ((Tx1-kx)<0):
    AT1szogo=AT1szogu+180
elif ((Ty1-ky)<0) and ((Tx1-kx)>0):
    AT1szogo=AT1szogu+360
       
AT1szogd=int(AT1szogo)
AT1szogm=int((AT1szogo-int(AT1szogd))*60)
AT1szogs=int(round((((AT1szogo-AT1szogd)*60)-AT1szogm)*60))

at1szog = math.degrees(AT1szogd + (AT1szogm/60) + (AT1szogs/3600))
AT1szog = at1szog/360*2*math.pi

tAT1 = round((math.sqrt(((Ty1-ky)**2)+((Tx1-kx)**2))),2)

########################Irányszög A-T2####################################

AT2szogu=math.degrees(math.atan((Ty2-ky)/(Tx2-kx)))
        
if ((Ty2-ky)>0) and ((Tx2-kx)>0):
    AT2szogo=AT2szogu
elif ((Ty2-ky)>0) and ((Tx2-kx)<0):
    AT2szogo=AT2szogu+180
elif ((Ty2-ky)<0) and ((Tx2-kx)<0):
    AT2szogo=AT2szogu+180
elif ((Ty2-ky)<0) and ((Tx2-kx)>0):
    AT2szogo=AT2szogu+360
       
AT2szogd=int(AT2szogo)
AT2szogm=int((AT2szogo-int(AT2szogd))*60)
AT2szogs=int(round((((AT2szogo-AT2szogd)*60)-AT2szogm)*60))

at2szog = math.degrees(AT2szogd + (AT2szogm/60) + (AT2szogs/3600))
AT2szog = at2szog/360*2*math.pi

tAT2 = round((math.sqrt(((Ty2-ky)**2)+((Tx2-kx)**2))),2)

###########################Irányszög B-T1#############################

BT1szogu=math.degrees(math.atan((Ty3-vy)/(Tx3-vx)))
        
if ((Ty3-vy)>0) and ((Tx3-vx)>0):
    BT1szogo=BT1szogu
elif ((Ty3-vy)>0) and ((Tx3-vx)<0):
    BT1szogo=BT1szogu+180
elif ((Ty3-vy)<0) and ((Tx3-vx)<0):
    BT1szogo=BT1szogu+180
elif ((Ty3-vy)<0) and ((Tx3-vx)>0):
    BT1szogo=BT1szogu+360
       
BT1szogd=int(BT1szogo)
BT1szogm=int((BT1szogo-int(BT1szogd))*60)
BT1szogs=int(round((((BT1szogo-BT1szogd)*60)-BT1szogm)*60))

bt1szog = math.degrees(BT1szogd + (BT1szogm/60) + (BT1szogs/3600))
BT1szog = bt1szog/360*2*math.pi

tBT1 = round((math.sqrt(((Ty3-vy)**2)+((Tx3-vx)**2))),2)

###########################Irányszög B-T2#############################

BT2szogu=math.degrees(math.atan((Ty4-vy)/(Tx4-vx)))
        
if ((Ty4-vy)>0) and ((Tx4-vx)>0):
    BT2szogo=BT2szogu
elif ((Ty4-vy)>0) and ((Tx4-vx)<0):
    BT2szogo=BT2szogu+180
elif ((Ty4-vy)<0) and ((Tx4-vx)<0):
    BT2szogo=BT2szogu+180
elif ((Ty4-vy)<0) and ((Tx4-vx)>0):
    BT2szogo=BT2szogu+360
       
BT2szogd=int(BT2szogo)
BT2szogm=int((BT2szogo-int(BT2szogd))*60)
BT2szogs=int(round((((BT2szogo-BT2szogd)*60)-BT2szogm)*60))

bt2szog = math.degrees(BT2szogd + (BT2szogm/60) + (BT2szogs/3600))
BT2szog = bt2szog/360*2*math.pi

tBT2 = round((math.sqrt(((Ty4-vy)**2)+((Tx4-vx)**2))),2)

#####################Törésszög Z számítás##########################

fzAT1 = AT1szog - LAT1szog

if(fzAT1 < 0):
    zAT1 = fzAT1 + 360
else:
    zAT1 = fzAT1
##
fzAT2 = AT2szog - LAT2szog

if(fzAT2 < 0):
    zAT2 = fzAT2 + 360
else:
    zAT2 = fzAT2
##    
fzBT1 = BT1szog - LBT1szog

if(fzBT1 < 0):
    zBT1 = fzBT1 + 360
else:
    zBT1 = fzBT1
##    
fzBT2 = BT2szog - LBT2szog

if(fzBT2 < 0):
    zBT2 = fzBT2 + 360
else:
    zBT2 = fzBT2

#####################Közepelés Súlyozva##############################

Akozep = ((zAT1*(tAT1/100)) + (zAT2*(tAT2/100)))/(tAT1/100 + tAT2/100)
Bkozep = ((zBT1*(tBT1/100)) + (zBT2*(tBT2/100)))/(tBT1/100 + tBT2/100)

######################P pontra menő irányszögek######################

fAPszog = LAPszog + Akozep

if (fAPszog > 360):
    APszog = fAPszog - 360
else:
    APszog = fAPszog

fBPszog = LBPszog + Bkozep

if(fBPszog > 360):
    BPszog = fBPszog - 360
else:
    BPszog = fBPszog

######################Alfa Béta Gamma szögek#########################

if (ABszog < 180):
    Alfa = APszog - ABszog
else:
    Alfa = ABszog - APszog

if (BAszog < 180):
    Beta = BPszog - BAszog
else:
    Beta = BAszog - BPszog

Gamma = 180 - (Alfa + Beta)

#######################Sinusos távolságok###########################

sinalfa = math.sin(math.radians(Alfa))
sinbeta = math.sin(math.radians(Beta))
singamma = math.sin(math.radians(Gamma))

tAP = (sinbeta / singamma) * tAB
tBP = (sinalfa / singamma) * tAB

#######################P pont koordinátái###########################

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

print("Leolvasas AT1 szog : ",LAT1szog)
print("Leolvasas AT2 szog : ",LAT2szog)
print("Leolvasas BT1 szog : ",LBT1szog)
print("Leolvasas BT2 szog : ",LBT2szog ,"\n")
print("tAB : ",tAB)
print("AB szog : ",ABszog)
print("BA szog : ",BAszog)
print("\n TAJEKOZAS A PONTON \n")
print("tAT1 : ",tAT1)
print("AT1 szog : ",AT1szog)
print("\ntAT2 : ",tAT2)
print("AT2 szog : ",AT2szog)
print("\ntBT1 : ",tBT1)
print("BT1 szog : ",BT1szog)
print("\ntBT2 : ",tBT2)
print("BT1 szog : ",BT2szog)
print("\n TORESSZOG Z SZAMITAS \n")
print("zAT1 : ",zAT1)
print("zAT2 : ",zAT2 ,"\n")
print("zBT1 : ",zBT1)
print("zBZ2 : ", zBT2, "\n")
print("\n KOZEPELES SULYOZVA \n")
print("Akozep : ",Akozep)
print("Bkozep : ",Bkozep)
print("\n P PONTRA MENO IRANYSZOG \n")
print("AP szog : ",APszog)
print("BP szog : ",BPszog)
print("\n BELSO SZOGEK \n")
print("Alfa : ",Alfa)
print("Beta : ",Beta)
print("Gamma : ",Gamma)
print("\n SINUSOS TAVOLSAGOK \n")
print("tAP : ",tAP)
print("tBP : ",tBP)
print("\n P PONT KOORDINATAI \n")
print("Ayv : ",Ayv)
print("Axv : ",Axv, "\n")
print("Byv : ",Byv)
print("Bxv : ",Bxv, "\n")
print("Y : ",y)
print("X : ",x)
