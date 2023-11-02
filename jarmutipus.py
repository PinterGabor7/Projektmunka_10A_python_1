from random import randint 
from valtozok import *
import os
os.system('cls')
def tipus():
    utasok = 0
    jarmutipus = randint(1, 4)
    match jarmutipus:
        case 1 :
            tipus = randint(1,3)
            utasok = randint(1,4)
        case 2 :
            tipus = randint(4,5)
            utasok = 1
        case 3 :
            tipus = randint(6,8)
            utasok = randint(1, 30)
        case 4 :
            tipus = randint(9,11)
            utasok = 1

    return(tipus, utasok)


