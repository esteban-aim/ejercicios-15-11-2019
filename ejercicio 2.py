print("cual es tu edad")
edad = int(input())

if edad >= 65:
    print("eres ansiano")
elif edad >= 45:
    print("eres adulto")
elif edad  >= 25:
    print("eres joven adulto")
elif edad >= 18:
    print("eres joven")
elif edad >= 8:
    print("eres niño")
elif edad >= 3:
    print("eres chiquillo ")
else:
    print("eres bebe")