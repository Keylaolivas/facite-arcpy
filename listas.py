#_*_ coding: utf-8_*_
#definir una lista con los dias de la semana
dias_semana = ['martes', 'miercoles', 'jueves', 'viernes', 'sabado']

print dias_semana

#agregarle un nuevo elemento a la lista al final
dias_semana.append('domingo')
dias_semana.insert(0,'lunes')

print dias_semana

#agregar una tupla
dias_semana.append( (1,2,3,4,5,6,7) )

print dias_semana

#borramos la tupla
dias_semana.pop(-1)

print dias_semana

dias_semana.remove('jueves')
print dias_semana

#ordenar la lista de manera ascendete

dias_semana.sort()
print dias_semana
dias_semana.sort(reverse=True)
print dias_semana


total_lista = dias_semana.count('sabado')
print "el sabado se encontro " + str(total_lista) + " veces"

total= len(dias_semana)
print "la lista de semanas tiene " + str(total) + " elementos"
