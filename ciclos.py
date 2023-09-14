# _*_ coding: utf-8 _*_
from random import randint
lista_aleatorios = []
for i in range (0, 101, 1):
    aleatorio = randint(0, 1000)
    lista_aleatorios.append(aleatorio)
print lista_aleatorios

if lista_aleatorios.count(100) < 0:
    print "Si se encontro el 100 en la lista 🎃 "
else:
    print "No tuvimos suerte princesa 👷‍♀️"