import sys
sys.path.append("src")
from LiquidadorNomina import FuncionesDeCalculo

from flask import Flask, request, jsonify


app = Flask(__name__)
salario_minimo = 1300000
subsidio_transporte = 162000
porcentaje_aporte_salud = 0.04
porcentaje_aporte_pension = 0.04
porcentaje_extra_diurno = 0.25
porcentaje_extra_nocturno = 0.75
porcentaje_extra_festivo = 0.75
porcentaje_valor_de_incapacidad = 1.0

@app.route('/capturar_datos', methods=['POST'])
def capturar_datos():
    # Capturar los datos enviados desde el formulario
    nombre = request.form['nombre']
    salario_base = float(request.form['salario-base'])
    tiempo_laborado = float(request.form['tiempo-laborado'])
    tiempo_festivo = float(request.form['tiempo-festivo'])
    licencias = float(request.form['licencias'])
    horas_extra_diurnas = float(request.form['horas-extras-diurnas'])
    horas_extra_nocturnas = float(request.form['horas-extras-nocturnas'])
    horas_extra_festivos = float(request.form['horas-extras-festivas'])
    incapacidades = float(request.form['incapacidades'])
    nomina = calcular_liquidacion_nomina(horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, incapacidades, salario_base, licencias, tiempo_laborado, tiempo_festivo)
    # Aquí puedes llamar a tu función con los datos capturados
    resultado = nomina    
    # Devolver el resultado como respuesta
    return jsonify({"resultado": resultado})

def calcular_liquidacion_nomina(horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos,tiempo_incapacidades, salario_base_mensual,tiempo_licencias_no_remuneradas, tiempo_laborado, tiempo_festivo_laborado):
    """Calcula la liquidación de la nómina."""
    valor_hora_laborada = salario_base_mensual / 192
    valor_salario = valor_hora_laborada * tiempo_laborado
    valor_hora_extra_diurna = FuncionesDeCalculo.calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas)
    valor_hora_extra_nocturna = FuncionesDeCalculo.calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas)
    valor_hora_extra_festivo = FuncionesDeCalculo.calcular_valor_hora_extra_festivo(valor_hora_laborada, horas_extra_festivos)
    valor_dias_festivos = FuncionesDeCalculo.calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado)
    valor_incapacidad = FuncionesDeCalculo.calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades)
    valor_licencia_no_remunerada = FuncionesDeCalculo.calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas)
    valor_aporte_a_salud = ((valor_salario) + (subsidio_transporte) +(valor_dias_festivos)+(valor_hora_extra_diurna)+(valor_hora_extra_nocturna)+(valor_hora_extra_festivo)) * porcentaje_aporte_salud
    valor_aporte_a_pension = ((valor_salario) + (subsidio_transporte) +(valor_dias_festivos)+(valor_hora_extra_diurna)+(valor_hora_extra_nocturna)+(valor_hora_extra_festivo)) * porcentaje_aporte_pension
    valor_fondo_solidaridad_pensional = FuncionesDeCalculo.calcular_valor_fondo_solidaridad_pensional(salario_base_mensual)

if __name__ == '__main__':
    app.run()

