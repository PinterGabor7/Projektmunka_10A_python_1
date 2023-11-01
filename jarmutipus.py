from random import randint 
from valtozok import *
import os
os.system('cls')
def tipus():
    utasok = 0
    jarmutipus = randint(1, 4)
    print(tipusa)
    match jarmutipus:
        case 1 :
            tipus = randint(1,3)
            utasok = randint(1,4)
            match tipus:
                case 1:
                    tipusa = 1
                    utasszam = utasok
                case 2:
                    tipusa = 2
                    utasszam = utasok
                case 3:
                    tipusa = 3
                    utasszam = utasok
        case 2 :
            tipus = randint(4,5)
            utasok = 1
            match tipus:
                case 4:
                    tipusa = 4
                    utasszam = utasok
                case 5:
                    tipusa = 5
                    utasszam = utasok
        case 3 :
            tipus = randint(6,8)
            utasok = randint(1, 30)
            match tipus:
                case 6:
                    tipusa = 6
                    utasszam = utasok
                case 7:
                    tipusa = 7
                    utasszam = utasok
                case 8:
                    tipusa = 8
                    utasszam = utasok
        case 4 :
            tipus = randint(9,11)
            utasok = 1
            match tipus:
                case 9:
                    tipusa = 9
                    utasszam = utasok
                case 10:
                    tipusa = 10
                    utasszam = utasok
                case 11:
                    tipusa = 11
                    utasszam = utasok

    return

    




tipus()


