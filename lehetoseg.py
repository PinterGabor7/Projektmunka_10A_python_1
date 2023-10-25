from random import randint
import os

def lehetosegek(tipus : int):
    print('A lehetőségek: ')
    if tipus > 8:
        print('\t1.: személyi')
        print('\t2.: táska átnézése')
        print('\t3.: zsebek átvizsgálása')
        valasztas = input('Választásom: ')
        while valasztas != '1' and valasztas != '2' and valasztas != '3':
            valasztas = input('Választásom: ')
    else:
        print('\tPapírok : \n\t\t1.: személyi \n\t\t2.: jogsi \n\t\t3.: forgalmi')
        print('\t4.: Csomagtartó megnézése')
        match tipus:        # a jármű típusa alapján plusz kérdés
            case 1:
                print('\t5.: Működik a fényszóró?')
            case 2:
                print('\t5.: Nincs semmi elvámolandó önöknél?')
            case 3:
                print('\t5.: Mit dolgozik?')
            case 4:
                print('\t5.: Mit szállít?')
            case 5:
                print('\t5.: Milyen cégtől szállít?')
            case 6:
                print('\t5.: Milyen iskolából vannak?')
            case 7:
                print('\t5.: Hova mennek?')
            case 8:
                print('\t5.: Honnan szállítják a rabokat?')
            case 9:
                print('\t5.: Miért megy át a határon?')
            case 10:
                print('\t5.: Van önnél bukósisak?')
            case 11:
                print('\t5.: Jól működik a fék?')
        print('\t6.: Átengedem')
        print('\t7.: Nem engedem át')
        valasztas = input('Választásom: ')
        while valasztas != '1' and valasztas != '2' and valasztas != '3' and valasztas != '4' and valasztas != '5' and valasztas != '6' and valasztas != '7':
            valasztas = input('Választásom: ')
    return int(valasztas)




