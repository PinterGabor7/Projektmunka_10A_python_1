from random import randint 
import os
os.system('cls')
def tipus():
    adatok = [0, 0]
    tipus = 0
    utasok = 0
    jarmutipus = randint(1, 4)
    match jarmutipus:
        case 1 :
            tipus = randint(1,3)
            utasok = randint(1,4)
            match tipus:
                case 1:
                    tipus = 'Tragacs'
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 2:
                    tipus = 'Családi autó'
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 3:
                    tipus = 'Limuzin'
                    adatok [0] = tipus
                    adatok [1] = utasok
        case 2 :
            tipus = randint(4,5)
            utasok = 1
            match tipus:
                case 4:
                    tipus = 'Furgon'
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 5:
                    tipus = 'Kamion'
                    adatok [0] = tipus
                    adatok [1] = utasok
        case 3 :
            tipus = randint(6,8)
            utasok = randint(1, 30)
            match tipus:
                case 6:
                    tipus = 'Iskolai Busz'
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 7:
                    tipus = 'Távolsági Busz'
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 8:
                    tipus = 'Rabszállító Busz'
                    adatok [0] = tipus
                    adatok [1] = utasok
        case 4 :
            tipus = randint(9,11)
            utasok = 1
            match tipus:
                case 9:
                    tipus = 'Gyalog'
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 10:
                    tipus = 'Bicikli'
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 11:
                    tipus = 'Roller'
                    adatok [0] = tipus
                    adatok [1] = utasok



    return adatok







