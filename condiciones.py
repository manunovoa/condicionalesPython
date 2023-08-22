nombreUsuario=input("Digite su nombre: ")

#Casteo de datos (convertir un dato en otro)
edadUsuario=int(input("Digite tu edad: "))

if edadUsuario>=18:
    print(f"{nombreUsuario} eres mayor de edad.")
else:
    print(f"{nombreUsuario} eres menor de edad.")
    print(f"{nombreUsuario} no puedes entrar a la disco.")

print("Continua el programa...")