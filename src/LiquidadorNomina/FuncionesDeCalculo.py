# Variables globales
salario_minimo = 1300000
subsidio_transporte = 162000
porcentaje_aporte_salud = 0.04
porcentaje_aporte_pension = 0.04
porcentaje_extra_diurno = 0.25
porcentaje_extra_nocturno = 0.75
porcentaje_extra_festivo = 0.75
porcentaje_valor_de_incapacidad = 1.0

def calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas):
    """Calcula el valor de la hora extra diurna."""
    return (valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_diurno)) * horas_extra_diurnas

def calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas):
    """Calcula el valor de la hora extra nocturna."""
    return (valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_nocturno)) * horas_extra_nocturnas

def calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo):
    """Calcula el valor de la hora extra festiva."""
    return (valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_festivo)) * valor_hora_extra_festivo

def calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado):
    """Calcula el valor de los dias festivos laborados."""
    return (8*(valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_festivo))) * tiempo_festivo_laborado

def calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades):
    """Calcula el valor de las incapacidades."""
    if tiempo_incapacidades <= 2:
        return (valor_hora_laborada * 8) * tiempo_incapacidades
    elif tiempo_incapacidades <= 90:
        return ((valor_hora_laborada * 8) * tiempo_incapacidades) * 0.6666
    else:
        return ((valor_hora_laborada * 8) * tiempo_incapacidades) * 0.5

def calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas):
    """Calcula el valor de las licencias no remuneradas."""
    return ((valor_hora_laborada * 8) * tiempo_licencias_no_remuneradas)

def calcular_valor_fondo_solidaridad_pensional(salario_base_mensual):
    """Calcula el valor al fondo de solidaridad pensional."""
    smmlv = salario_base_mensual / salario_minimo
    if smmlv > 20:
        return salario_base_mensual * 0.02
    elif 19 < smmlv <= 20:
        return salario_base_mensual * 0.018
    elif 18 < smmlv <= 19:
        return salario_base_mensual * 0.016
    elif 17 < smmlv <= 18:
        return salario_base_mensual * 0.014
    elif 16 < smmlv <= 17:
        return salario_base_mensual * 0.012
    elif 4 < smmlv <= 16:
        return salario_base_mensual * 0.01
    else:
        return 0
    
    