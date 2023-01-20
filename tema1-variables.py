# Este es un comentario

n1="23"
n2="24"

a=123
b=23.5
c="roberto"

# conversion estricta de datos
#int() float() str()
#suma
print(int(n1)+int(n2))

print(int(b))

#da error porque el dato interno no es un enterio sino un flotante
valor="123"
print(int(valor))

valor="123"
print(int(str(valor)))

valor="123"
print(len(str(valor)))
