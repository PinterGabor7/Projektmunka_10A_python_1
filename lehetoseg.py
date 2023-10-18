from random import randint
import os

def auto_lehetosegek():
    print('A lehetőségek: ')
    print('\t1.: Papírok : 1.: személyi / 2.: jogsi / 3.: forgali')
    print('\t3.: Csomagtartó megnézése')
    print('\t4.: Átengedem')
    print('\t5.: Nem engedem át')
    valasztas = input('Választásom: ')
    while valasztas != '1' and valasztas != '2' and valasztas != '3' and valasztas != '4' and valasztas != '5':
        valasztas = input('Választásom: ')
    return int(valasztas)
        


