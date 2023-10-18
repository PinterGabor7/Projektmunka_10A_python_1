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
            tipus = randint(1,4)
            utasok = randint(1,4)
            match tipus:
                case 1:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 2:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 3:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 4:
                    adatok [0] = tipus
                    adatok [1] = utasok
        case 2 :
            tipus = randint(5,6)
            utasok = 1
            match tipus:
                case 5:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 6:
                    adatok [0] = tipus
                    adatok [1] = utasok
        case 3 :
            tipus = randint(7,9)
            utasok = randint(1, 20)
            match tipus:
                case 7:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 8:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 9:
                    adatok [0] = tipus
                    adatok [1] = utasok
        case 4 :
            tipus = randint(10,12)
            utasok = 1
            match tipus:
                case 10:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 11:
                    adatok [0] = tipus
                    adatok [1] = utasok
                case 12:
                    adatok [0] = tipus
                    adatok [1] = utasok



    return adatok
asd = tipus()
print(f'{asd [0], asd [1]}')







