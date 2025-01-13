# Programa para calcular el área de un rombo y un hexágono.
# Utiliza diferentes tipos de datos (integer, float, string, boolean) y sigue la convención snake_case.
# Incluye comentarios para explicar la lógica del código.

import math  # Importamos la librería math para usar funciones matemáticas como sqrt.

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    """
    Calcula el área de un rombo utilizando sus diagonales.
    Fórmula: Área = (diagonal_mayor * diagonal_menor) / 2
    """
    if diagonal_mayor <= 0 or diagonal_menor <= 0:  # Validación de valores positivos.
        return "Las diagonales deben ser valores positivos."
    area = (diagonal_mayor * diagonal_menor) / 2  # Cálculo del área.
    return area


def calcular_area_hexagono(lado):
    """
    Calcula el área de un hexágono regular utilizando la longitud de su lado.
    Fórmula: Área = (3 * sqrt(3) * lado^2) / 2
    """
    if lado <= 0:  # Validación de valores positivos.
        return "El lado debe ser un valor positivo."
    area = (3 * math.sqrt(3) * lado**2) / 2  # Cálculo del área.
    return area


def main():
    """
    Función principal que interactúa con el usuario y muestra los resultados.
    """
    print("Bienvenido al calculador de áreas para un rombo y un hexágono.")

    # Solicitar datos para el rombo.
    diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))

    # Calcular y mostrar el área del rombo.
    area_rombo = calcular_area_rombo(diagonal_mayor, diagonal_menor)
    if isinstance(area_rombo, str):  # Si el resultado es un mensaje de error.
        print(area_rombo)
    else:
        print(f"El área del rombo es: {area_rombo:.2f}")  # Mostrar el área con 2 decimales.

    # Solicitar datos para el hexágono.
    lado_hexagono = float(input("Ingrese la longitud del lado del hexágono: "))

    # Calcular y mostrar el área del hexágono.
    area_hexagono = calcular_area_hexagono(lado_hexagono)
    if isinstance(area_hexagono, str):  # Si el resultado es un mensaje de error.
        print(area_hexagono)
    else:
        print(f"El área del hexágono es: {area_hexagono:.2f}")  # Mostrar el área con 2 decimales.


if __name__ == "__main__":
    main()  # Ejecutar la función principal.