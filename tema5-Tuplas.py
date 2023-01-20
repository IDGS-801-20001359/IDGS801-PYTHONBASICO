 #solo se usan parentesis para la tupla
#definicion de una tupla con tres elementos
tupla=(1,2,3)
print(tupla)
print(type(tupla)) #para saber que tipo de dato es, si es una tupla una lista o un diccionario

tupla2=(7,"Roberto",True,23.8,16+7j)
print(tupla2)

print(tupla2[1]) #muestra el indice de una tupla

print(tupla2[4]) #ultimo elemento de una tupla definiendo en que numero esta
print(tupla2[-1]) #ultimo elemento de una tupla recorriendo el numero
print(tupla2[0:3]) #otra manera de agarrar elementos es definiendo de un numero a otro con dos puntos
print(tupla2[:3]) #no necesitas especificar el inicio
print(tupla2[3:]) #o asi desde el tres hasta terminal

a,b,c=tupla #es una estructuracion
print(a)
print(c)

tuplaN=tupla+tupla2 #sumar ambas tuplas
print(tuplaN)
print(tupla.count(2)) #count contar el numero de aparienciones de un elemento

#una vez que agregaste ya tu tupla ya no puedes cambiar el valor queriendo agregarle mas cosas 
tupla[2]=23


