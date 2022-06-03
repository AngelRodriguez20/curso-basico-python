    #Declaramos una variable
calificacion = input("Introduce tu calificacion del AZ-900:")

calificacion = int(calificacion)

    #Preguntamos si la calificacion es menor a 700
if calificacion < 700 : 
    print("Por no estudiar") # Si es menor a 700, muestra esto
elif calificacion > 1000 : 
    print("Mientes no puedes sacar mas de 1000")
else: # Si no se cumple el if anterior, pasa a esta linea 
    print("Felicidades")

# Verificador de mayoria de edad
edad = input("Introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 115 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes con tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esa coca")

    # En python no hay switch case