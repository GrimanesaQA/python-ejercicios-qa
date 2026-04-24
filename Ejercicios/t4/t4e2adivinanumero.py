
def eligenumero(numero):
    if (numero == 4):
        mensaje = "Victoria, has acertado"
    if (numero != 4):
        mensaje = "Derrota, has fallado"
    return mensaje


numero = int(input("Elige un número entre 1 y 10:" ))
mensaje = eligenumero(numero)
print(mensaje)