"""Offset_kelvin significa "Desplazamiento"""
OFFSET_KELVIN = 273.15
 
MENU = (
    "Seleccione una opción:\n"
    "1--> Capturar Temperatura\n"
    "2--> Celsius a Fahrenheit\n"
    "3--> Celsius a Kelvin\n"
    "4--> Kelvin a Fahrenheit\n"
    "5--> Kelvin a Celsius\n"
    "6--> Fahrenheit a Kelvin\n"
    "7--> Fahrenheit a Celsius\n"
    "0--> Salir\n"
)

def parar():
    """Detiene el programa hasta que el usuario presione ENTER."""
    input("Presione <ENTER> para continuar")


def capturar():
    """Solicita una temperatura al usuario y la retorna como float.

    Si el valor ingresado no es numérico, muestra el error y retorna None.
    """
    try:
        return float(input("Por favor digite la temperatura: "))
    except ValueError as error:
        print(error)
        return None


def celsius_fahrenheit(celsius):
    """Convierte grados Celsius a grados Fahrenheit: F = (C * 9/5) + 32."""
    return (celsius * 9 / 5) + 32


def celsius_kelvin(celsius):
    """Convierte grados Celsius a Kelvin: K = C + 273.15."""
    return celsius + OFFSET_KELVIN


def kelvin_fahrenheit(kelvin):
    """Convierte Kelvin a grados Fahrenheit: F = (K - 273.15) * 9/5 + 32."""
    return (kelvin - OFFSET_KELVIN) * 9 / 5 + 32


def kelvin_celsius(kelvin):
    """Convierte Kelvin a grados Celsius: C = K - 273.15."""
    return kelvin - OFFSET_KELVIN


def fahrenheit_kelvin(fahrenheit):
    """Convierte grados Fahrenheit a Kelvin: K = (F - 32) * 5/9 + 273.15."""
    return (fahrenheit - 32) * 5 / 9 + OFFSET_KELVIN


def fahrenheit_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius: C = (F - 32) * 5/9."""
    return (fahrenheit - 32) * 5 / 9


def main():
    """Ejecuta el menú principal del programa."""
    continuar = True
    temperatura = 0
    """No sea Weon"""
    while continuar:
        opcion = input(MENU)
        if opcion == "1":
            temperatura = capturar()
        elif opcion == "2":
            print(f"{temperatura}°C = {celsius_fahrenheit(temperatura)} °F")
            parar()
        elif opcion == "3":
            print(f"{temperatura}°C = {celsius_kelvin(temperatura)} °K")
            parar()
        elif opcion == "4":
            print(f"{temperatura}°K = {kelvin_fahrenheit(temperatura)} °F")
            parar()
        elif opcion == "5":
            print(f"{temperatura}°K = {kelvin_celsius(temperatura)} °C")
            parar()
        elif opcion == "6":
            print(f"{temperatura}°F = {fahrenheit_kelvin(temperatura)} °K")
            parar()
        elif opcion == "7":
            print(f"{temperatura}°F = {fahrenheit_celsius(temperatura)} °C")
            parar()
        elif opcion == "0":
            print("Bye")
            continuar = False
        else:
            print("Seleccione una opción válida")

if __name__ == "__main__":
    main()
