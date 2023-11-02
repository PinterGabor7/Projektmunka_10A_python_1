import random,os
from jarmutipus import *
from lehetoseg import *
from valtozok import *

while penz < 500:
    os.system('cls')
    ido = 480
    penz -= 5
    penz += kereset

    while ido < 1080:
        os.system('cls')
        tapasztalatpont += 1
        rangneve = ''

        if  tapasztalatpont<= 10:
            rangneve = 'Újonc'
        elif   tapasztalatpont>= 10 and tapasztalatpont<= 24:
            rangneve = 'Kezdő'
        elif   tapasztalatpont>= 25 and tapasztalatpont<= 44:
            rangneve = 'Haladó'
        elif   tapasztalatpont>= 45 and tapasztalatpont<= 63:
            rangneve = 'Profi'
        elif   tapasztalatpont>= 64:
            rangneve = 'Veterán'

        print(f'\t\t\t\tstats: \tpénz={penz}Bitcoin\t\t\t idő={int((ido-ido%60)/60)} óra {ido%60} perc \n \t\t\t\t\t életkedv={eletkedv} \t teljesítmény= {teljesitmeny}% \trang = {rangneve}')

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
        if (tipusa > 8 and (valasztas_1 == 5 or valasztas_1 == 6)) or (tipusa <= 8 and (valasztas_1 == 6 or valasztas_1 == 7)):
            if (tipusa > 8 and valasztas_1 == 5 and jo_ember) or (tipusa >= 8 and valasztas_1 == 6 and not jo_ember) or (tipusa <= 8 and valasztas_1 == 6 and jo_ember) or (tipusa < 8 and valasztas_1 == 7 and not jo_ember):
                kereset += 1
            else:
                kereset -= 1
        else:
            valasztas_2 = atenged(jo_ember, tipusa, valasztas_1)
            while valasztas_2 == 3:
                os.system('cls')
                ido += 10
                valasztas_1 = lehetosegek(tipusa)
                if (tipusa > 8 and (valasztas_1 == 5 or valasztas_1 == 6)) or (tipusa <= 8 and (valasztas_1 == 6 or valasztas_1 == 7)):
                    break
                valasztas_2 = atenged(jo_ember, tipusa, valasztas_1)
            if valasztas_2 == 3:
                if (tipusa > 8 and valasztas_1 == 5 and jo_ember) or (tipusa > 8 and valasztas_1 == 5 and not jo_ember) or (tipusa <= 8 and valasztas_1 == 6 and jo_ember) or (tipusa <= 8 and valasztas_1 == 7 and not jo_ember):
                    kereset += 1
                else:
                    kereset -= 1
            else:
                if (valasztas_2 == 1 and jo_ember) or (valasztas_2 == 2 and not jo_ember):
                    kereset += 1
                else:
                    kereset -= 1


