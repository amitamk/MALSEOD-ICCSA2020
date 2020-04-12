# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:57:42 2020

@author: Ami
"""

import shelve

filename = 'D:\\Amita\\Doutorado\\Tese\\Traduzido\\testeshelve.out'

nome ='Amita'
idade = 40

my_shelf = shelve.open(filename,'n') # 'n' for new

for key in dir(nome):
    try:
        if (key=='nome') or (key=='idade'):
            my_shelf[key] = globals()[key]
    except TypeError:
        #
        # __builtins__, my_shelf, and imported modules can not be shelved.
        #
        print('ERROR shelving: {0}'.format(key))
my_shelf.close()

# PARA RECUPERAR:

my_shelf = shelve.open(filename)

for key in my_shelf:
    globals()[key]=my_shelf[key]

my_shelf.close()

