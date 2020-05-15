from Database import *
# print()
x = lambda x: True if x in film else False
for film in afiseaza_numar_filme():
    if x('drama'):
        print(film)


