import sys
sys.path.append("src")
from LiquidadorNomina import FuncionesDeEntradaySalida, LiquidadorNominaCode


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nMenú:")
    print("1. Calcular liquidación de nómina")
    print("2. Modificar parámetros")
    print("3. Como usar")
    print("4. Salir")

def main():
    """Función principal del programa."""
    print("Bienvenido al sistema de liquidación de nómina")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            LiquidadorNominaCode.calcular_liquidacion_nomina()

        elif opcion == "2":
            LiquidadorNominaCode.modificar_parametros()

        elif opcion == "3":
            FuncionesDeEntradaySalida.mostrar_como_usar()

        elif opcion == "4":
            print("Gracias por usar el sistema de liquidación de nómina")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
