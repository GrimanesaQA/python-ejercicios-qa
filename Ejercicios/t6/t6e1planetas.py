
planetas = ["Júpiter", "Marte", "Mercurio", "Neptuno", "Saturno", "Tierra", "Urano", "Venus"]

numero = int(input("Elige un número del 1 al 8:" ))

if numero >= 1 and numero <= 8:
    print("El planeta es:", planetas[numero - 1])
else:
    print("Error")


