#Hacer un programa en Python en el cual se ingrese una temperatura en grados
#Celsius y se convierta a Fahrenheit, Kelvin y a Rankine.
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_rankine(celsius):
    return (celsius + 273.15) * 1.8

def convertir_temperatura():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    print("La temperatura en grados Fahrenheit es:", celsius_to_fahrenheit(celsius))
    print("La temperatura en grados Kelvin es:", celsius_to_kelvin(celsius))
    print("La temperatura en grados Rankine es:", celsius_to_rankine(celsius))

continuar = True
while continuar:
    convertir_temperatura()
    respuesta = input("¿Desea continuar? (s/n)")
    if respuesta.lower() == "n":
        continuar = False
print("Hasta luego!")
