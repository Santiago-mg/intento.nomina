import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from LiquidadorNomina.FuncionesDeCalculo import calcular_valor_dias_festivos, calcular_valor_fondo_solidaridad_pensional, calcular_valor_hora_extra_diurna, calcular_valor_hora_extra_nocturna, calcular_valor_hora_extra_festivo, calcular_valor_incapacidad, calcular_valor_licencia_no_remunerada

class TestCalculadoraDeNomina(unittest.TestCase):

    #-----------------------------Funcion calcular_valor_hora_extra_diurna_normal
    def test_calcular_valor_hora_extra_diurna_normal(self):
        casos_prueba = [
            (10000, 2, 25000),  
            (20000, 3, 75000), 
            (15000, 1, 18750)
        ]
        for valor_hora_laborada, horas_extra_diurnas, expected in casos_prueba:
            self.assertEqual(calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas), expected)

    def test_calcular_valor_hora_extra_diurna_extraordinario(self):
        casos_prueba = [
            (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
            (10000, 0, 0),  # caso extraordinario: horas extra diurnas es 0
            (-10000, 2, -25000)  # caso extraordinario: valor de hora laborada es negativo
        ]
        for valor_hora_laborada, horas_extra_diurnas, expected in casos_prueba:
            self.assertEqual(calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas), expected)

    def test_calcular_valor_hora_extra_diurna_error(self):
        casos_prueba = [
            ("10000", 2),  # caso de error: valor de hora laborada no es un número
            (10000, "2"),  # caso de error: horas extra diurnas no es un número
            (None, 2),  # caso de error: valor de hora laborada es None
            (10000, None)  # caso de error: horas extra diurnas es None
        ]
        for valor_hora_laborada, horas_extra_diurnas in casos_prueba:
            with self.assertRaises(TypeError):
                calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas)

    #-----------------------------Funcion calcular_valor_hora_extra_nocturna_normal
    def test_calcular_valor_hora_extra_nocturna_normal(self):
        casos_prueba = [
            (10000, 2, 35000), 
            (20000, 3, 105000),  
            (15000, 1, 26250)
        ]
        for valor_hora_laborada, horas_extra_nocturnas, expected in casos_prueba:
            self.assertEqual(calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas), expected)

    def test_calcular_valor_hora_extra_nocturna_extraordinario(self):
        casos_prueba = [
            (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
            (10000, 0, 0),  # caso extraordinario: horas extra nocturnas es 0
            (-10000, 2, -35000)  # caso extraordinario: valor de hora laborada es negativo
        ]
        for valor_hora_laborada, horas_extra_nocturnas, expected in casos_prueba:
            self.assertEqual(calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas), expected)

    def test_calcular_valor_hora_extra_nocturna_error(self):
        casos_prueba = [
            ("10000", 2),  # caso de error: valor de hora laborada no es un número
            (10000, "2"),  # caso de error: horas extra nocturnas no es un número
            (None, 2),  # caso de error: valor de hora laborada es None
            (10000, None)  # caso de error: horas extra nocturnas es None
        ]
        for valor_hora_laborada, horas_extra_nocturnas in casos_prueba:
            with self.assertRaises(TypeError):
                calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas)

#-----------------------------Funcion calcular_valor_hora_extra_festivo
    def test_calcular_valor_hora_extra_festivo_normal(self):
        casos_prueba = [
            (10000, 2, 35000),  
            (20000, 3, 105000), 
            (15000, 1, 26250)
        ]
        for valor_hora_laborada, valor_hora_extra_festivo, expected in casos_prueba:
            self.assertEqual(calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo), expected)

    def test_calcular_valor_hora_extra_festivo_extraordinario(self):
        casos_prueba = [
            (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
            (10000, 0, 0),  # caso extraordinario: valor de hora extra festivo es 0
            (-10000, 2, -35000)  # caso extraordinario: valor de hora laborada es negativo
        ]
        for valor_hora_laborada, valor_hora_extra_festivo, expected in casos_prueba:
            self.assertEqual(calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo), expected)

    def test_calcular_valor_hora_extra_festivo_error(self):
        casos_prueba = [
            ("10000", 2),  # caso de error: valor de hora laborada no es un número
            (10000, "2"),  # caso de error: valor de hora extra festivo no es un número
            (None, 2),  # caso de error: valor de hora laborada es None
            (10000, None)  # caso de error: valor de hora extra festivo es None
        ]
        for valor_hora_laborada, valor_hora_extra_festivo in casos_prueba:
            with self.assertRaises(TypeError):
                calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo)

    #-----------------------------Funcion calcular_valor_dias_festivos
    def test_calcular_valor_dias_festivos_normal(self):
        casos_prueba = [
            (10000, 2, 280000), 
            (20000, 3, 840000),  
            (15000, 1, 210000)
        ]
        for valor_hora_laborada, tiempo_festivo_laborado, expected in casos_prueba:
            self.assertEqual(calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado), expected)

    def test_calcular_valor_dias_festivos_extraordinario(self):
        casos_prueba = [
            (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
            (10000, 0, 0),  # caso extraordinario: tiempo festivo laborado es 0
            (-10000, 2, -280000)  # caso extraordinario: valor de hora laborada es negativo
        ]
        for valor_hora_laborada, tiempo_festivo_laborado, expected in casos_prueba:
            self.assertEqual(calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado), expected)

    def test_calcular_valor_dias_festivos_error(self):
        casos_prueba = [
            ("10000", 2),  # caso de error: valor de hora laborada no es un número
            (10000, "2"),  # caso de error: tiempo festivo laborado no es un número
            (None, 2),  # caso de error: valor de hora laborada es None
            (10000, None)  # caso de error: tiempo festivo laborado es None
        ]
        for valor_hora_laborada, tiempo_festivo_laborado in casos_prueba:
            with self.assertRaises(TypeError):
                calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado)

    #-----------------------------Funcion calcular_valor_incapacidad
    def test_calcular_valor_incapacidad_normal(self):
        casos_prueba = [
            (10000, 2, 160000),  
            (20000, 1, 160000), 
            (15000, 3, 239976)
        ]
        for valor_hora_laborada, tiempo_incapacidades, expected in casos_prueba:
            self.assertEqual(calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades), expected)

    def test_calcular_valor_incapacidad_extraordinario(self):
        casos_prueba = [
            (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
            (10000, 0, 0),  # caso extraordinario: tiempo de incapacidades es 0
            (-10000, 2, -160000)  # caso extraordinario: valor de hora laborada es negativo
        ]
        for valor_hora_laborada, tiempo_incapacidades, expected in casos_prueba:
            self.assertEqual(calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades), expected)

    def test_calcular_valor_incapacidad_error(self):
        casos_prueba = [
            ("80-000@", 4),  # caso de error: valor de hora laborada no es un número
            (10000, "2"),  # caso de error: tiempo de incapacidades no es un número
            (None, 2),  # caso de error: valor de hora laborada es None
            (10000, None)  # caso de error: tiempo de incapacidades es None
        ]
        for valor_hora_laborada, tiempo_incapacidades in casos_prueba:
            with self.assertRaises(TypeError):
                calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades)

    #-----------------------------Funcion calcular_valor_licencia_no_remunerada
    def test_calcular_valor_licencia_no_remunerada_normal(self):
        casos_prueba = [
            (10000, 2, 160000), 
            (20000, 3, 480000),  
            (15000, 1, 120000)
        ]
        for valor_hora_laborada, tiempo_licencias_no_remuneradas, expected in casos_prueba:
            self.assertEqual(calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas), expected)

    def test_calcular_valor_licencia_no_remunerada_extraordinario(self):
        casos_prueba = [
            (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
            (10000, 0, 0),  # caso extraordinario: tiempo de licencias no remuneradas es 0
            (-10000, 2, -160000)  # caso extraordinario: valor de hora laborada es negativo
        ]
        for valor_hora_laborada, tiempo_licencias_no_remuneradas, expected in casos_prueba:
            self.assertEqual(calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas), expected)

    def test_calcular_valor_licencia_no_remunerada_error(self):
        casos_prueba = [
            ("vuevemil", "a2"),  # caso de error: valor de hora laborada no es un número
            ("1000a0", "s"),  # caso de error: tiempo de licencias no remuneradas no es un número
            (None, 2),  # caso de error: valor de hora laborada es None
            (10000, None)  # caso de error: tiempo de licencias no remuneradas es None
        ]
        for valor_hora_laborada, tiempo_licencias_no_remuneradas in casos_prueba:
            with self.assertRaises(TypeError):
                calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas)

    #-----------------------------Funcion calcular_valor_fondo_solidaridad_pensional
    def test_calcular_valor_fondo_solidaridad_pensional_normal(self):
        casos_prueba = [
            (1000000, 0), 
            (4000000, 0), 
            (5000000, 0)
        ]
        for salario_base_mensual, expected in casos_prueba:
            self.assertEqual(calcular_valor_fondo_solidaridad_pensional(salario_base_mensual), expected)

    def test_calcular_valor_fondo_solidaridad_pensional_extraordinario(self):
        casos_prueba = [
            (0, 0),  # caso extraordinario: salario base mensual es 0
            (-1000000, 0),  # caso extraordinario: salario base mensual es negativo
            (10000000, 100000)  # caso extraordinario: salario base mensual es muy alto
        ]
        for salario_base_mensual, expected in casos_prueba:
            self.assertEqual(calcular_valor_fondo_solidaridad_pensional(salario_base_mensual), expected)

    def test_calcular_valor_fondo_solidaridad_pensional_error(self):
        casos_prueba = [
            ("1000000"),  # caso de error: salario base mensual no es un número
            (None),  # caso de error: salario base mensual es None
            ("mil"),  # caso de error: salario base mensual es una cadena no numérica
            ("10ty0")  # caso de error: salario base mensual no es un número
        ]
        for salario_base_mensual in casos_prueba:
            with self.assertRaises(TypeError):
                calcular_valor_fondo_solidaridad_pensional(salario_base_mensual)

# Ejecuta las pruebas si este archivo se ejecuta como un script
if __name__ == '__main__':
    unittest.main()
































# Funciones que se deben probar unitariamente:

#     Funciones de cálculo (como calcular_valor_hora_extra_diurna, calcular_valor_incapacidad, etc.): Estas funciones realizan cálculos basados en parámetros de entrada.

# Funciones que no necesitan pruebas unitarias:

#     Funciones de presentación (mostrar_informacion, modificar_parametros, mostrar_menu): Estas funciones se encargan de la presentación de datos al usuario o la modificación de variables globales. 

#     Función principal (main): La función principal interactúa con otras funciones y maneja el flujo de ejecución del programa. 