#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(1, r'C:\Users\basil\PycharmProjects\c04-ch6-exercices-bASILgIL')
from exercice_2 import frequence

# TODO: Définissez vos fonction ici
def volume_masse(a=3, b=5, c=6, p= 3.3):
    volume = (4/3)* math.pi * a * b * c
    masse = volume * p

    return volume, masse




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(volume_masse())
    #voir pq ca fonctionne pas --print(f"Le volume de l'ellipsoide est de {volume} m^3 et sa masse est de {masse} kg.")
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("bbbig bbbig test"))
    #print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("ceci est une phrase"))
    print(frequence("phrases"))