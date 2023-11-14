import random,os,sys
from jarmutipus import *
from lehetoseg import *
from valtozok import *
from bevezeto import *


def statok():
    global kereset
    global teljesitmeny
    rangneve = ''
    if  tapasztalatpont<= 10:
        rangneve = 'Újonc'
    elif   tapasztalatpont>= 10 and tapasztalatpont<= 24:
        rangneve = 'Kezdő'
        kereset = 10
    elif   tapasztalatpont>= 25 and tapasztalatpont<= 44:
        rangneve = 'Haladó'
        kereset = 15
    elif   tapasztalatpont>= 45 and tapasztalatpont<= 63:
        rangneve = 'Profi'
        kereset = 20
    elif   tapasztalatpont>= 64:
        rangneve = 'Veterán'
        kereset = 25
    if jol_atengedett + rosszul_atengedett > 0:
        teljesitmeny = jol_atengedett / (jol_atengedett + rosszul_atengedett)*100
    else:
        teljesitmeny = 100
    
    if ido%60 < 10:    
        print('--------------------------------------------------------------------------------------------------')
        print(f'  pénz = {penz}€      idő: {int((ido-ido%60)/60)}:0{ido%60}      kereset = {kereset}       teljesítmény = {teljesitmeny:.2f}%      rang: {rangneve}')
        print('--------------------------------------------------------------------------------------------------\n')
    else:
        print('--------------------------------------------------------------------------------------------------')
        print(f'  pénz = {penz}€      idő: {int((ido-ido%60)/60)}:{ido%60}      kereset = {kereset}       teljesítmény = {teljesitmeny:.2f}%      rang: {rangneve}')
        print('--------------------------------------------------------------------------------------------------\n')

bevezeto = bevezeto()
print(f'{bevezeto}')

while penz < 150:
    os.system('cls')
    ido = 480
    penz -= 6
    penz += kereset
    napok += 1

    while ido < 1080 and penz < 200:
        os.system('cls')
        statok()
        tapasztalatpont += 1
        adatok = tipus()
        tipusa = adatok[0]
        utasszam = adatok[1]
        jarmu_tipus = ''
        match tipusa:
            case 1:
                jarmu_tipus = "Régi autó"
            case 2:
                jarmu_tipus = "Személyautó"
            case 3:
                jarmu_tipus = "Sportautó"
            case 4:
                jarmu_tipus = "Kis furgon"
            case 5:
                jarmu_tipus = "Kamion"
            case 6:
                jarmu_tipus = "Iskolásokat szállító busz"
            case 7:
                jarmu_tipus = "Távolsági busz"
            case 8:
                jarmu_tipus = "Rabszállító busz"

        if tipusa < 9:
            print('Új jármű érkezett.')
            print(f'Jármű típusa: {jarmu_tipus}')
            print(f'Utasok száma: {utasszam}')
        else:
            match tipusa:
                case 9:
                    print('Érkezett egy gyalogos')
                case 10:
                    print('Érkezett egy biciklis')
                case 11:
                    print('Érkezett egy rolleres')

        jo_ember = randint(0,1)
        
        ido += 30


        valasztas_1 = lehetosegek(tipusa)
        if (tipusa > 8 and valasztas_1 == 7) or (tipusa <= 8 and valasztas_1 == 8):
            sys.exit()
        if (tipusa > 8 and (valasztas_1 == 5 or valasztas_1 == 6)) or (tipusa <= 8 and (valasztas_1 == 6 or valasztas_1 == 7)):
            if (tipusa > 8 and valasztas_1 == 5 and jo_ember) or (tipusa >= 8 and valasztas_1 == 6 and not jo_ember) or (tipusa <= 8 and valasztas_1 == 6 and jo_ember) or (tipusa < 8 and valasztas_1 == 7 and not jo_ember):
                jol_atengedett += 1
            else:
                rosszul_atengedett += 1
        else:
            valasztas_2 = atenged(jo_ember, tipusa, valasztas_1)
            while valasztas_2 == 3:
                os.system('cls')
                statok()
                ido += 10
                valasztas_1 = lehetosegek(tipusa)
                if (tipusa > 8 and valasztas_1 == 7) or (tipusa <= 8 and valasztas_1 == 8):
                    sys.exit()
                if (tipusa > 8 and (valasztas_1 == 5 or valasztas_1 == 6)) or (tipusa <= 8 and (valasztas_1 == 6 or valasztas_1 == 7)):
                    break
                valasztas_2 = atenged(jo_ember, tipusa, valasztas_1)
            if valasztas_2 == 4:
                sys.exit()
            if valasztas_2 == 3:
                if (tipusa > 8 and valasztas_1 == 5 and jo_ember) or (tipusa > 8 and valasztas_1 == 5 and not jo_ember) or (tipusa <= 8 and valasztas_1 == 6 and jo_ember) or (tipusa <= 8 and valasztas_1 == 7 and not jo_ember):
                    jol_atengedett += 1
                else:
                    rosszul_atengedett += 1
            else:
                if (valasztas_2 == 1 and jo_ember) or (valasztas_2 == 2 and not jo_ember):
                    jol_atengedett += 1
                else:
                    rosszul_atengedett += 1

print(f'\n{teljesitmeny:.2f}%-ban engedted át helyesen az embereket.')
print(f'{jol_atengedett} jó embert engedtél át.')
print(f'{rosszul_atengedett} rossz embert engedtél át.')
print(f'{napok} játékbeli napba telt kivinned a játékot.\n')

