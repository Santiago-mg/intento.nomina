def solicitar_dato_de_parametro(mensaje, tipo_dato=float):
    """Solicita un dato al usuario y maneja las excepciones."""
    while True:
        try:
            dato = tipo_dato(input(mensaje))
            if dato < 0:
                print("El dato no puede ser negativo. Inténtalo de nuevo.")
                continue
            return dato
        except ValueError:
            print(f"Entrada inválida. Por favor, ingresa un número{' entero' if tipo_dato is int else ''}.")

def solicitar_datos_entrada():
    """Solicita los datos de entrada al usuario."""
    salario_base_mensual = solicitar_dato_de_parametro("Ingrese el salario básico mensual: ")
    tiempo_laborado = solicitar_dato_de_parametro("Ingrese el tiempo laborado al mes en horas: ")
    tiempo_festivo_laborado = solicitar_dato_de_parametro("Ingrese el tiempo festivo laborado en días: ")
    horas_extra_diurnas = solicitar_dato_de_parametro("Ingrese las horas extras diurnas laboradas: ")
    horas_extra_nocturnas = solicitar_dato_de_parametro("Ingrese las horas extras nocturnas laboradas: ")
    horas_extra_festivos = solicitar_dato_de_parametro("Ingrese las horas extras festivas laboradas: ")
    tiempo_incapacidades = solicitar_dato_de_parametro("Ingrese el tiempo de incapacidades en días: ", int)
    tiempo_licencias_no_remuneradas = solicitar_dato_de_parametro("Ingrese el tiempo de licencias no remuneradas en días: ", int)

    return salario_base_mensual, tiempo_laborado, tiempo_festivo_laborado, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, tiempo_incapacidades, tiempo_licencias_no_remuneradas


def mostrar_informacion(valor_salario, subsidio_transporte, valor_hora_extra_diurna, valor_hora_extra_nocturna, valor_hora_extra_festivo, valor_dias_festivos, valor_incapacidad, valor_licencia_no_remunerada, valor_aporte_a_salud, valor_aporte_a_pension, valor_fondo_solidaridad_pensional):
    """Muestra la información calculada en pantalla."""

    total_ingresos = valor_salario + subsidio_transporte + valor_dias_festivos + valor_hora_extra_diurna + valor_hora_extra_nocturna + valor_hora_extra_festivo + valor_incapacidad
    total_deducciones = valor_licencia_no_remunerada + valor_aporte_a_salud + valor_aporte_a_pension + valor_fondo_solidaridad_pensional
    total_neto = total_ingresos - total_deducciones
    
    print("\nInformación de liquidación de nómina:")
    print(f"Salario: {valor_salario}")
    print(f"Subsidio de transporte: {subsidio_transporte}")
    print(f"Valor días festivos: {valor_dias_festivos}")
    print(f"Valor horas extras diurnas: {valor_hora_extra_diurna}")
    print(f"Valor horas extras nocturnas: {valor_hora_extra_nocturna}")
    print(f"Valor horas extras festivas: {valor_hora_extra_festivo}")
    print(f"Valor de incapacidades: {valor_incapacidad}")
    print(f"Valor de licencia no remunerada: {valor_licencia_no_remunerada}")
    print(f"Valor aporte a salud: {valor_aporte_a_salud}")
    print(f"Valor aporte a pensión: {valor_aporte_a_pension}")
    print(f"Valor al fondo de solidaridad pensional: {valor_fondo_solidaridad_pensional}")
    print(f"Total a pagar/neto: {total_neto}")

def mostrar_como_usar():
    """Muestra las instrucciones de uso."""
    try:
        with open('resources/como_usar.txt', 'r', encoding='utf-8') as file:
            mensaje = file.read()
            print(mensaje)
    except FileNotFoundError:
        print("El archivo 'como_usar.txt' no se encontró en la carpeta 'recursos'.")
