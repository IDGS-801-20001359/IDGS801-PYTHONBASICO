
texto1="Hola"
texto2="Mundo!!"
textoFinal= texto1+" "+texto2
print(textoFinal)

print("El saludo es: %s %s" % (texto1,texto2))

# Con o sin numeros dentro de las llaves puedes especificar el orden de la frase
cadena="Saludar dos: {1} {0} ".format(texto1,texto2)
print(cadena)

# Otra forma de poner las palabras con X y Y
cadena="Saludar dos: {x} {y} ".format(x=texto1,y=texto2)
print(cadena)