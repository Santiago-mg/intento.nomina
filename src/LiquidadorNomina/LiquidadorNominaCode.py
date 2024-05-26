import os
from .FuncionesDeCalculo import *
from .FuncionesDeEntradaySalida import *

def solicitar_dato_de_parametro(mensaje, default=None, tipo_dato=float):
    """Solicita un dato al usuario y maneja las excepciones."""
    while True:
        dato = input(mensaje)
        if dato.upper() == "DEF":
            return default
        try:
            dato = tipo_dato(dato)
            if dato < 0:
                print("El dato no puede ser negativo. Inténtalo de nuevo.")
                continue
            return dato
        except ValueError:
            print(f"Entrada inválida. Por favor, ingresa un número{' entero' if tipo_dato is int else ''}.")

def modificar_parametros():
    """Permite al usuario modificar los parámetros globales."""
    global salario_minimo,subsidio_transporte, porcentaje_aporte_salud, porcentaje_aporte_pension, porcentaje_extra_diurno, porcentaje_extra_nocturno, porcentaje_extra_festivo
    print("\nModificar parámetros:")

    salario_minimo = solicitar_dato_de_parametro("Nuevo valor del salario minimo (DEF para dejar como está): ", salario_minimo)
    subsidio_transporte = solicitar_dato_de_parametro("Nuevo valor de subsidio de transporte (DEF para dejar como está): ", subsidio_transporte)
    porcentaje_aporte_salud = solicitar_dato_de_parametro("Nuevo % de aporte a salud (DEF para dejar como está): ", porcentaje_aporte_salud)
    porcentaje_aporte_pension = solicitar_dato_de_parametro("Nuevo % de aporte a pensión (DEF para dejar como está): ", porcentaje_aporte_pension)
    porcentaje_extra_diurno = solicitar_dato_de_parametro("Nuevo % de valor de hora extra diurna (DEF para dejar como está): ", porcentaje_extra_diurno)
    porcentaje_extra_nocturno = solicitar_dato_de_parametro("Nuevo % de valor de hora extra nocturna (DEF para dejar como está): ", porcentaje_extra_nocturno)
    porcentaje_extra_festivo = solicitar_dato_de_parametro("Nuevo % de valor de hora extra festiva (DEF para dejar como está): ", porcentaje_extra_festivo)

    print("Parámetros modificados correctamente.")

def calcular_liquidacion_nomina():
    """Calcula la liquidación de la nómina."""
    salario_base_mensual, tiempo_laborado, tiempo_festivo_laborado, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, tiempo_incapacidades, tiempo_licencias_no_remuneradas = solicitar_datos_entrada()
    valor_hora_laborada = salario_base_mensual / 192
    valor_salario = valor_hora_laborada * tiempo_laborado
    valor_hora_extra_diurna = calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas)
    valor_hora_extra_nocturna = calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas)
    valor_hora_extra_festivo = calcular_valor_hora_extra_festivo(valor_hora_laborada, horas_extra_festivos)
    valor_dias_festivos = calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado)
    valor_incapacidad = calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades)
    valor_licencia_no_remunerada = calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas)
    valor_aporte_a_salud = ((valor_salario) + (subsidio_transporte) +(valor_dias_festivos)+(valor_hora_extra_diurna)+(valor_hora_extra_nocturna)+(valor_hora_extra_festivo)) * porcentaje_aporte_salud
    valor_aporte_a_pension = ((valor_salario) + (subsidio_transporte) +(valor_dias_festivos)+(valor_hora_extra_diurna)+(valor_hora_extra_nocturna)+(valor_hora_extra_festivo)) * porcentaje_aporte_pension
    valor_fondo_solidaridad_pensional = calcular_valor_fondo_solidaridad_pensional(salario_base_mensual)

    mostrar_informacion(valor_salario, subsidio_transporte, valor_hora_extra_diurna, valor_hora_extra_nocturna, valor_hora_extra_festivo, valor_dias_festivos, valor_incapacidad, valor_licencia_no_remunerada, valor_aporte_a_salud, valor_aporte_a_pension, valor_fondo_solidaridad_pensional)
