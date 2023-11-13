from random import randint
from valtozok import *
import os

def lehetosegek(tipus : int):
    print('A lehetőségek: ')
    if tipus > 8:
        print('\t1.: személyi')
        print('\t2.: táska átnézése')
        print('\t3.: zsebek átvizsgálása')
        match tipus:
            case 9:
                print('\t4.: Miért megy át a határon?')
            case 10:
                print('\t4.: Van önnél bukósisak?')
            case 11:
                print('\t4.: Jól működik a fék?')
        print('\t5.: Átengedem')
        print('\t6.: Nem engedem át')
        print('\t7.: Kilépés')
        valasztas = input('Választásom: ')
        while valasztas != '1' and valasztas != '2' and valasztas != '3' and valasztas != '4' and valasztas != '5' and valasztas != '6' and valasztas != '7':
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
        print('\t6.: Átengedem')
        print('\t7.: Nem engedem át')
        print('\t8.: Kilépés')
        valasztas = input('Választásom: ')
        while valasztas != '1' and valasztas != '2' and valasztas != '3' and valasztas != '4' and valasztas != '5' and valasztas != '6' and valasztas != '7' and valasztas != '8':
            valasztas = input('Választásom: ')
    return int(valasztas)


def atenged(jo: bool, tipus: int, kerdes: int):
    print()
    if not jo:
        if tipus > 8:
            match kerdes:
                case 1:
                    print('Neve: Kala Pál\nAnyja neve: Kala Júlia\nSzületési dátum: 2003.02.29\nSzületési hely: Pápa')
                case 2:
                    print('Táska tartalma: telefon, szendvics, pénztárca, kulacs, rugós kés')
                case 3:
                    print('Jobb zseb: telefon\nBal zseb: pénztárca, fülhallgató, egy tasak kábítószer')
                case 4:
                    match tipus:
                        case 9:
                            print('Mert köröznek, de csak kisértékű lopásért.')
                        case 10:
                            print('Nincs, kellene?')
                        case 11:
                            print('Egyáltalán nem, de a cipőtalpam jól tapad.')

        else:
            match kerdes:
                case 1:
                    print('Neve: Kalim Pál\nAnyja neve: Kalim Katalin\nSzületési dátum: 2003.03.03\nSzületési hely: Misoklc')
                case 2:
                    print('A1-es jogosítvány: nincs\nB1-es jogosítvány: van\n\tMegszerzési dátum: 2023.12.12')
                case 3:
                    print('Autó márkája: Tesla\nB kategóriájú jogosítvány megszerzése: 2020.10.10\nÜzemanyag: Benzin\nEurotax kód: GBD4327')
                case 4:
                    print('Csomagtartó tartalma: bőrönd, roller, teniszütő, pisztoly')
                case 5:
                    match tipus:
                        case 1:
                            print('A jobb igen, de a bal sajnos nem.')
                        case 2:
                            print('Nincs, csak egy cipőt, egy aranygyűrűt és egy biciklit vettünk.')
                        case 3:
                            print('Biciklikerekeket szerelek a Volvo-nál.')
                        case 4:
                            print('Cigarettát és marihuánát Hollandiából.')
                        case 5:
                            print('Az Audiból telefont.')
                        case 6:
                            print('A győri Princeton-ból.')
                        case 7:
                            print('A Kékesre, Ausztriába.')
                        case 8:
                            print('A tatabányai börtönből.')

    else:
        if tipus > 8:
            match kerdes:
                case 1:
                    print('Neve: Rúgka Pál\nAnyja neve: Rúgka Borbála\nSzületési dátum: 1998.04.04.\nSzületési hely: Tatabánya')
                case 2:
                    print('Táska tartalma: telefon, szendvics, pénztárca, kulacs, rágó')
                case 3:
                    print('Jobb zseb: telefon\nBal zseb: pénztárca, fülhallgató')
                case 4:
                    match tipus:
                        case 9:
                            print('Hogy meglátogassam a bácsikámat, itt él a határ mellett.')
                        case 10:
                            print('Igen, csak az ellenőrzéshez levettem.')
                        case 11:
                            print('Persze, nyugodtan megvizsgálhatja.')
        else:
            match kerdes:
                case 1:
                    print('Neve: Szlo Pál\nAnyja neve: Szlo Anett\nSzületési dátum: 2003.03.03\nSzületési hely: Budapest')
                case 2:
                    print('A1-es jogosítvány: nincs\nB1-es jogosítvány: van\n\tMegszerzési dátum: 2023.09.09.')
                case 3:
                    print('Autó márkája: Mazda\nB kategóriájú jogosítvány megszerzése: 2020.10.10\nÜzemanyag: Benzin\nEurotax kód: GBD4327')
                case 4:
                    print('Csomagtartó tartalma: bőrönd, roller, teniszütő')
                case 5:
                    match tipus:
                        case 1:
                            print('Igen, ha szeretné fel is kapcsolom.')
                        case 2:
                            print('Nincs, nem vettünk semmit.')
                        case 3:
                            print('Kerekeket rögzítek a Volvo-nál')
                        case 4:
                            print('Különböző halakat: lazacot, pisztrángot és sügért.')
                        case 5:
                            print('Az Audiból, Győrből.')
                        case 6:
                            print('A Győri SZC Jedlik Ányos Gépipari és Informatikai Technikum és Kollégiumból')
                        case 7:
                            print('Ausztriába a hegyekbe.')
                        case 8:
                            print('A győri börtönből.')

    print('\nLehetőségek: ')
    print('\t1.: Átengedem')
    print('\t2.: Nem engedem át')
    print('\t3.: Újabb kérdés')
    print('\t4.: Kilépés')
    valasztas = input('Választásom: ')
    while valasztas != '1' and valasztas != '2' and valasztas != '3' and valasztas != '4':
        valasztas = input('Választásom: ')
    return int(valasztas)


