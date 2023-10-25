import random,os
from jarmutipus import *
from lehetoseg import *
from valtozok import *
tipus = tipus()

print('Új jármű érkezett.')
print(f'Jármű típusa: {tipus[0]}')
print(f'Utasok száma: {tipus[1]}')
kereset= 0
penz = 20
eletkedv = 100
teljesitmeny = 50
tapasztalatpont = 0
ido = 480
rangneve = ''
napikoltseg = 1

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




print(f'\t\t\t\tstats: \tpénz={penz}Bitcoin\t\t\t idő={ido} perc \n \t\t\t\t\t életkedv={eletkedv} \t teljesítmény= {teljesitmeny}% \trang = {rangneve}')


