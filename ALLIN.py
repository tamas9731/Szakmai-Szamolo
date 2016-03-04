import math
import os, sys

def PolarisPont():
    os.system("cls")
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

        input("\nEnter vissza a menube")
        menu()
    else:
        os.system("cls")
        
        print("HIBA")
        print("A fok nagyobb mint 360")
        print("Egy perc vagy masodperc nagyobb mint 60")
        input("\nEnter vissza a menube")
        menu()

def Iranyszog():
    os.system("cls")
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

    input("\nEnter vissza a menube")
    menu()

def BelsoszogesElometszes():
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

    if ((Alfad < 360) or (Alfam < 60) or (Alfas < 60) or (Betad < 360) or (Betam < 60) or (Betas < 60)):
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
            
        #Irányszög B-A

        if (ABszog > 180):
            BAszog = ABszog - 180
        else:
            BAszog = ABszog + 180

        sinalf = math.sin(math.radians(Alfaszog))
        sinbet = math.sin(math.radians(Betaszog))
        singam = math.sin(math.radians(Gammaszog))


        tAP = (sinbet / singam) * tAB
        tBP = (sinalf / singam) * tAB

        APszog = ABszog + Alfaszog
        BPszog = BAszog - Betaszog

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

        os.system("cls")
        
        print(y)
        print(x)

        input("\nEnter vissza a menube")
        menu()
        
    else:
        os.system("cls")
        
        print("HIBA")
        print("A fok nagyobb mint 360")
        print("Egy perc vagy masodperc nagyobb mint 60")
        input("\nEnter vissza a menube")
        menu()
        
def Ivmetszes():
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

    print(y)
    print(x)

def menu():
    os.system("cls")
    
    Figyelem = "\nMinden beirt adat beiras utan torlodik a keprol es csak az eredmeny latszik\n"
    print("1, Polasris Pont.")
    print("2, Iranyszog, Tavolsag Koordinatabol.")
    print("3, Belsoszoges Elometszes.")
    print("4, Ivmetszes.")
    print(Figyelem)
    print("A tavolsagok meterbe jelennek meg")
    valaszt = int(input("Valassz : "))
    
    if valaszt == 1:
        PolarisPont()        
        
    if valaszt == 2:
        Iranyszog()

    if valaszt == 3:
        BelsoszogesElometszes()

    if valaszt == 4:
        Ivmetszes()

    

menu()
