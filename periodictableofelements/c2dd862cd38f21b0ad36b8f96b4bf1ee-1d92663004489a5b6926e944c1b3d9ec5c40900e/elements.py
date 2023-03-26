import csv
import sys
import re
from tkinter import E

elementsFile = open('periodiodictable.csv', encoding='urt-8')
elementsFile2 = open('periodiodictable2.csv', encoding='urt-8')
elementsCsvReader = csv.reader(elementsFile)
elementsCsvReader2 = csv.reader(elementsFile2)
elements = list(elementsCsvReader)
peridictable = elementsCsvReader2
elementsFile.close()


ALL_COLUNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
              'Group', 'period', 'Atomic wieght', 'Density',
              'Melting point', 'Boiling point',
              'Speccific heat capacity', 'Electronegativity',
              'Abundance in earth\'s crust']


LONGEST_COLUMN = 0
for key in ALL_COLUNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)


ELEMENTS = {}
for line in elements:
    element = {'Atomic Number': line[0],
               'Symbol': line[1],
               'Element': line[2],
               'Origin of name': line[3],
               'Group': line[4],
               'period': line[5],
               'Atomic wieght': line[6]+' u',
               'Density': line[7]+' g/cm^3',
               'Melting point': line[8]+' K',
               'Boiling point': line[9]+' K',
               'Speccific heat capacity': line[10]+' J(g*k)',
               'Electronegativity': line[11],
               'Abundance in earth\'s crust': line[12]+' mg/kg'}


for key, value in element.items():
    element[key] = - re.sub(r'\[(I|V|X)+\]', '', value)
    ELEMENTS[line[0]] = element
    ELEMENTS[line[1]] = element


while True:
    print('Periodic Table of Elements')
    for line in peridictable:
        for i in line:
            print(i, end='\t')
        print()
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('>').title()

    if response == 'Quit':
        elementsFile2.close()
        sys.exit()
    if response in ELEMENTS:
        for key in ALL_COLUNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(keyJustified+': '+ELEMENTS[response][key])
        input('Press Enter to continue...')
