
def sumar(num1,num2):
    print("{}+{}={}".format(num1,num2,num1+num2))

def restar(num1,num2):
    print("{}-{}={}".format(num1,num2,num1-num2))

def multiplicar(num1,num2):
    print("{}*{}={}".format(num1,num2,num1*num2))

def dividir(num1,num2):
    print("{}/{}={}".format(num1,num2,num1/num2))

def main():
    print("BIENVENIDO AL MENU \n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir")

if __name__ == "__main__":
    main()

opcion=int(input("Ingresa una opcion:"))

num1=int(input("Ingresa el primer número:"))
num2=int(input("Ingresa el segundo número:"))

while opcion!=5:
    if opcion == 1:
        sumar(num1,num2)
    elif opcion == 2:
        restar(num1,num2)
    elif opcion == 3:
        multiplicar(num1,num2)
    elif opcion == 4:
        dividir(num1,num2)
    else:
        print("La opcion elegida es erronea")
    
    main()
    opcion = int(input("Ingrese una opcion:"))

print("¡Gracias por su atencion!")

