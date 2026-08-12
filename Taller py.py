# 1
nombres = ["Juan", "Maria", "Pedro", "Luisa", "Carlos"]
nombre = input("Ingrese un nombre: ")

if nombre in nombres:
    print("Bienvenido,", nombre)
else:
    print("Nombre no registrado")

# 2
año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")

# 3
nombre = input("Ingrese su nombre: ")
cuenta = input("Ingrese su número de cuenta: ")
pin = input("Ingrese su PIN: ")

if len(cuenta) != 10:
    print("Error: el número de cuenta debe tener 10 dígitos")
elif len(pin) != 4:
    print("Error: el PIN debe tener 4 dígitos")
else:
    saldo = float(input("Ingrese su saldo actual: "))
    retiro = float(input("Ingrese el monto a retirar: "))

    if retiro > saldo:
        print("No hay fondos suficientes")
    elif retiro == saldo:
        print("Retiro exitoso, su cuenta quedará en cero")
        saldo = 0
    else:
        saldo = saldo - retiro
        print("Retiro exitoso")

    if saldo > 500000:
        clasificacion = "Cuenta saludable"
    elif saldo >= 100000:
        clasificacion = "Cuenta estable"
    elif saldo > 0:
        clasificacion = "Saldo bajo"
    else:
        clasificacion = "Cuenta en cero"

    print("----- COMPROBANTE -----")
    print("Nombre:", nombre)
    print("Cuenta:", cuenta)
    print("Monto retirado:", retiro)
    print("Saldo restante:", saldo)
    print("Clasificación:", clasificacion)

# 4
hora = int(input("Ingrese la hora (0-23): "))
dia = int(input("Ingrese el día (1-7): "))

if hora < 0 or hora > 23:
    print("Error: hora inválida")
elif dia < 1 or dia > 7:
    print("Error: día inválido")
else:
    if dia >= 1 and dia <= 5:
        if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
            trafico = "Hora pico"
        else:
            trafico = "Tráfico normal"
    else:
        trafico = "Tráfico bajo"

    if trafico == "Hora pico":
        tiempo = 90
    elif trafico == "Tráfico normal":
        tiempo = 60
    else:
        tiempo = 30

    lluvia = input("¿Está lloviendo? (si/no): ").lower()

    if lluvia == "si":
        if trafico == "Hora pico":
            tiempo = tiempo + 20
        else:
            tiempo = tiempo + 10

    print("----- REPORTE -----")
    print("Hora:", hora)
    print("Día:", dia)
    print("Tráfico:", trafico)
    print("Lluvia:", lluvia)
    print("Tiempo en verde:", tiempo)

    if tiempo > 100:
        print("Precaución: tiempo de espera alto para peatones")
    else:
        print("Flujo vehicular en condiciones normales")