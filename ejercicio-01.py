print("cual es tu nombre?")
nombre = input()
print("cual es tu apellido?")
apellido = input()
print("cual es tu edad?")
edad = int(input())

if edad >= 18:
    print("Hola " + nombre + " " + apellido + " eres mayor de edad")
else:
    print("Hola " + nombre + " " + apellido + " eres menor de edad")