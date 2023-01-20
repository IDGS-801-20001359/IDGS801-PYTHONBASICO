# arreglos que admite diferentes tipos de datos 
nombres=["Juan", "Mario", "Laura"]
numeros=[1,2,3,4,5]

datos=[1,2,5,"Mario",True]

nombres[0]="Roberto"

#formas de como puedo recorrer las palabras o tupla
print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

#agregar elemtnos nuevos a la lista
nombres.append("Dario")
print(nombres)
nombres.insert(2,"Maria")
print(nombres)

#esto es una cadena para agregar una palabra
nombres.extend(["Chencha",2,23,5])
print(nombres)

#esto es una cadena para eliminar una palabra
nombres.remove("Chencha")
print(nombres)
#esto es una cadena para eliminar una palabra
nombres.pop()
print(nombres)

# Multiplas cinco veces el nombre de juan
n=["Juan"]
n2=n*5
print(n2)
print(nombres)

#eliminame el primer elemento o el que quieras de la lista
del nombres[0]
print(nombres)



