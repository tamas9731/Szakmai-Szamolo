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
    os.system("cls")
    
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
        
        print("Y koordinata : ",y)
        print("X koordinata : ",x)

        input("\nEnter vissza a menube")
        menu()
        
    else:
        os.system("cls")
        
        print("HIBA")
        print("A fok nagyobb mint 360")
        print("Egy perc vagy masodperc nagyobb mint 60")
        input("\nEnter vissza a menube")
        menu()
def TajekozottElometszes():
    os.system("cls")
    
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
    LBT1szogs = int(input("BT1 leolvasas Masodperc"))

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

    os.system("cls")
    
    print("Y koordinata : ",y)
    print("X koordinata : ",x)

    input("\nEnter vissza a menube")
    menu()

def Ivmetszes():
    os.system("cls")
    
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

    os.system("cls")
    
    print("Y koordinata : ",y)
    print("X koordinata : ",x)

    input("\nEnter vissza a menube")
    menu()

def menu():
    os.system("cls")
    
    Figyelem = "\nMinden beirt adat beiras utan torlodik a keprol es csak az eredmeny latszik\n"
    print("1, Polasris Pont.")
    print("2, Iranyszog, Tavolsag Koordinatabol.")
    print("3, Belsoszoges Elometszes.")
    print("4, Ivmetszes.")
    print("5, Tajekozoiranyos Elometszes")
    print(Figyelem)
    print("A tavolsagok meterbe jelennek meg\n")
    valaszt = int(input("Valassz : "))
    
    if valaszt == 1:
        PolarisPont()        
        
    if valaszt == 2:
        Iranyszog()

    if valaszt == 3:
        BelsoszogesElometszes()

    if valaszt == 4:
        Ivmetszes()

    if valaszt == 5:
        TajekozottElometszes()
    

menu()
