from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.metrics import dp

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Crear un diseño principal vertical
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título de la aplicación
        header_label = Label(text="Liquidación de Nómina", font_size='20sp', bold=True, size_hint=(1, None), height=50, text_size=(None, None))
        main_layout.add_widget(header_label)

        # Crear dos diseños de cuadrícula para las entradas de datos
        input_layout1 = GridLayout(cols=2, row_default_height=40, row_force_default=True, spacing=10, padding=10, size_hint=(1, None), height=200, col_default_width=100)
        input_layout2 = GridLayout(cols=2, row_default_height=40, row_force_default=True, spacing=10, padding=10, size_hint=(1, None), height=200, col_default_width=100)

        # Agregar los campos de entrada al primer layout
        input_layout1.add_widget(Label(text="Salario base mensual:"))
        self.salario_input = TextInput(multiline=False)
        input_layout1.add_widget(self.salario_input)

        input_layout1.add_widget(Label(text="Tiempo laborado al mes (horas):"))
        self.tiempo_laborado_input = TextInput(multiline=False)
        input_layout1.add_widget(self.tiempo_laborado_input)

        input_layout1.add_widget(Label(text="Tiempo festivo laborado (días):"))
        self.tiempo_festivo_laborado_input = TextInput(multiline=False)
        input_layout1.add_widget(self.tiempo_festivo_laborado_input)

        input_layout1.add_widget(Label(text="Licencias no remuneradas (días):"))
        self.licencias_no_remuneradas_input = TextInput(multiline=False)
        input_layout1.add_widget(self.licencias_no_remuneradas_input)

        # Agregar los campos de entrada al segundo layout
        input_layout2.add_widget(Label(text="Horas extras diurnas laboradas:"))
        self.horas_extra_diurnas_input = TextInput(multiline=False)
        input_layout2.add_widget(self.horas_extra_diurnas_input)

        input_layout2.add_widget(Label(text="Horas extras nocturnas laboradas:"))
        self.horas_extra_nocturnas_input = TextInput(multiline=False)
        input_layout2.add_widget(self.horas_extra_nocturnas_input)

        input_layout2.add_widget(Label(text="Horas extras festivas laboradas:"))
        self.horas_extra_festivas_input = TextInput(multiline=False)
        input_layout2.add_widget(self.horas_extra_festivas_input)

        input_layout2.add_widget(Label(text="Incapacidades (días):"))
        self.incapacidades_input = TextInput(multiline=False)
        input_layout2.add_widget(self.incapacidades_input)

        # Añadir diseños de entradas al diseño principal
        main_layout.add_widget(input_layout1)
        main_layout.add_widget(input_layout2)

        # Espacio para los resultados
        resultado_layout = GridLayout(cols=2, spacing=10, padding=10)
        resultado_layout.bind(minimum_height=resultado_layout.setter('height'))
        main_layout.add_widget(resultado_layout)

        # Etiqueta para mostrar los resultados
        self.resultado_labels = []
        for i in range(6):
            label = Label(text="", valign='top', halign='left', size_hint=(1, None), height=dp(40))
            resultado_layout.add_widget(label)
            self.resultado_labels.append(label)

        for i in range(6):
            label = Label(text="", valign='top', halign='left', size_hint=(1, None), height=dp(40))
            resultado_layout.add_widget(label)
            self.resultado_labels.append(label)

        # Botón para calcular la nómina ubicado en la parte inferior de la aplicación
        self.calcular_button = Button(text="Calcular liquidación de nómina", size_hint=(1, None), height=40)
        self.calcular_button.bind(on_press=self.calcular_nomina)
        main_layout.add_widget(self.calcular_button)

        # Botón para limpiar los campos de entrada y los resultados
        self.limpiar_button = Button(text="Limpiar", size_hint=(1, None), height=40)
        self.limpiar_button.bind(on_press=self.limpiar_todo)
        main_layout.add_widget(self.limpiar_button)

        # Asignar el diseño principal a la pantalla
        self.add_widget(main_layout)

    def limpiar_todo(self, instance):
        # Limpiar todos los campos de entrada
        self.salario_input.text = ""
        self.tiempo_laborado_input.text = ""
        self.tiempo_festivo_laborado_input.text = ""
        self.licencias_no_remuneradas_input.text = ""
        self.horas_extra_diurnas_input.text = ""
        self.horas_extra_nocturnas_input.text = ""
        self.horas_extra_festivas_input.text = ""
        self.incapacidades_input.text = ""

        # Limpiar los resultados
        self.resultado_label.text = ""

    def validar_entrada(self, entrada, campo):
        """Intenta convertir una entrada a float. Devuelve None si falla."""
        try:
            valor = float(entrada)
            return valor, None
        except ValueError:
            return None, campo


    def mostrar_error(self, mensaje):
        """Muestra un mensaje de error en un Popup."""
        popup = Popup(title="Error",
                      content=Label(text=mensaje, size_hint=(0.5, 0.5)),
                      size_hint=(0.5, 0.5))
        popup.open()

    def formato(self, numero):
            numero_redondeado = round(numero, 2)
            if numero_redondeado == -0.0:
                numero_redondeado = abs(numero_redondeado)
            return f"{numero_redondeado:.2f}"

    def calcular_nomina(self, instance):
        # Validar las entradas
        salario_base_mensual, error_salario = self.validar_entrada(self.salario_input.text, "Salario base mensual")
        tiempo_laborado, error_tiempo = self.validar_entrada(self.tiempo_laborado_input.text, "Tiempo laborado al mes (horas)")
        tiempo_festivo_laborado, error_festivo = self.validar_entrada(self.tiempo_festivo_laborado_input.text, "Tiempo festivo laborado (días)")
        horas_extra_diurnas, error_diurnas = self.validar_entrada(self.horas_extra_diurnas_input.text, "Horas extras diurnas laboradas")
        horas_extra_nocturnas, error_nocturnas = self.validar_entrada(self.horas_extra_nocturnas_input.text, "Horas extras nocturnas laboradas")
        horas_extra_festivas, error_festivas = self.validar_entrada(self.horas_extra_festivas_input.text, "Horas extras festivas laboradas")
        incapacidades, error_incapacidades = self.validar_entrada(self.incapacidades_input.text, "Incapacidades (días)")
        licencias_no_remuneradas, error_licencias = self.validar_entrada(self.licencias_no_remuneradas_input.text, "Licencias no remuneradas (días)")

        # Verificar si alguna entrada es inválida
        if any(value is None for value in [salario_base_mensual, tiempo_laborado, tiempo_festivo_laborado, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivas, incapacidades, licencias_no_remuneradas]):
            if error_salario:
                self.mostrar_error(f"En {error_salario} ingresante un caracter no valido (letra)")
            elif error_tiempo:
                self.mostrar_error(f"En {error_tiempo} ingresante un caracter no valido (letra)")
            elif error_festivo:
                self.mostrar_error(f"En {error_festivo} ingresante un caracter no valido (letra)")
            elif error_diurnas:
                self.mostrar_error(f"En {error_diurnas} ingresante un caracter no valido (letra)")
            elif error_nocturnas:
                self.mostrar_error(f"En {error_nocturnas} ingresante un caracter no valido (letra)")
            elif error_festivas:
                self.mostrar_error(f"En {error_festivas} ingresante un caracter no valido (letra)")
            elif error_incapacidades:
                self.mostrar_error(f"En {error_incapacidades} ingresante un caracter no valido (letra)")
            elif error_licencias:
                self.mostrar_error(f"En {error_licencias} ingresante un caracter no valido (letra)")
            return

        # Variables de configuración (porcentajes y valores fijos)
        porcentaje_aporte_salud = 0.04  # 4% de aportes a salud
        porcentaje_aporte_pension = 0.04  # 4% de aportes a pensión
        subsidio_transporte = 162000  # Valor del subsidio de transporte (debe verificar el valor exacto)
        dias_trabajo_mensuales = 30

        # Calcular valores
        
        valor_hora_laborada = salario_base_mensual / 192
        valor_salario = valor_hora_laborada * tiempo_laborado
        valor_horas_extra_festivas = (valor_hora_laborada + (valor_hora_laborada * 0.75)) * horas_extra_festivas
        valor_días_festivos = (8*(valor_hora_laborada + (valor_hora_laborada * 0.75))) * tiempo_festivo_laborado
        valor_horas_extra_diurnas = (valor_hora_laborada + (valor_hora_laborada * 0.25)) * horas_extra_diurnas
        valor_horas_extra_nocturnas = (valor_hora_laborada + (valor_hora_laborada * 0.75)) * horas_extra_nocturnas
        valor_incapacidades = (valor_hora_laborada * 8) * incapacidades if incapacidades <= 2 else ((valor_hora_laborada * 8) * incapacidades * 0.6666 if incapacidades <= 90 else (valor_hora_laborada * 8 * incapacidades * 0.5)) 
        valor_licencias_no_remuneradas = ((valor_hora_laborada * 8) * licencias_no_remuneradas)

        # Calcular aportes a salud, pensión y fondo de solidaridad pensional
        base_de_aporte = valor_salario + subsidio_transporte + valor_días_festivos + valor_horas_extra_diurnas + valor_horas_extra_nocturnas + valor_horas_extra_festivas
        valor_aporte_a_salud = ((valor_salario) + (subsidio_transporte) +(valor_días_festivos)+(valor_horas_extra_diurnas)+(valor_horas_extra_nocturnas)+(valor_horas_extra_festivas)) * porcentaje_aporte_salud
        valor_aporte_a_pension = ((valor_salario) + (subsidio_transporte) +(valor_días_festivos)+(valor_horas_extra_diurnas)+(valor_horas_extra_nocturnas)+(valor_horas_extra_festivas)) * porcentaje_aporte_pension
        
        # Verifique si el salario base mensual excede los 4 salarios mínimos para determinar el fondo de solidaridad pensional
        salario_minimo_mensual = 1300000  # Suponga que este es el salario mínimo, ajuste según sea necesario
        smmlv = salario_base_mensual / salario_minimo_mensual
        valor_fondo_solidaridad_pensional = salario_base_mensual*0.02 if smmlv > 20 else (salario_base_mensual * 0.018 if 19 < smmlv <= 20 else (salario_base_mensual*0.016 if 18 < smmlv <= 19 else (salario_base_mensual*0.014 if 17<smmlv<=18 else (salario_base_mensual*0.012 if 16<smmlv<=17 else(salario_base_mensual*0.01 if 4<smmlv<=16 else(0))))))
        
        # Calcular totales
        total_ingresos = valor_salario + subsidio_transporte + valor_días_festivos + valor_horas_extra_diurnas + valor_horas_extra_nocturnas + valor_horas_extra_festivas + valor_incapacidades
        total_deducciones = valor_licencias_no_remuneradas + valor_aporte_a_salud + valor_aporte_a_pension + valor_fondo_solidaridad_pensional
        total_neto = total_ingresos - total_deducciones

                # Mostrar los resultados
        resultados_izquierda = [
            f"Salario base mensual: {self.formato(valor_salario)}",
            f"Subsidio de transporte: {self.formato(subsidio_transporte)}",
            f"Valor de días festivos: {self.formato(valor_días_festivos)}",
            f"Valor de horas extra diurnas: {self.formato(valor_horas_extra_diurnas)}",
            f"Valor de horas extra nocturnas: {self.formato(valor_horas_extra_nocturnas)}",
            f"Valor de horas extra festivas: {self.formato(valor_horas_extra_festivas)}"
        ]

        resultados_derecha = [
            f"Valor de incapacidades: {self.formato(valor_incapacidades)}",
            f"Valor de licencias no remuneradas: {self.formato(valor_licencias_no_remuneradas)}",
            f"Aporte a salud: {self.formato(valor_aporte_a_salud)}",
            f"Aporte a pensión: {self.formato(valor_aporte_a_pension)}",
            f"Fondo de solidaridad pensional: {self.formato(valor_fondo_solidaridad_pensional)}",
            f"Total neto a pagar: {self.formato(total_neto)}"
        ]

        for i, label in enumerate(self.resultado_labels[:6]):
            label.text = resultados_izquierda[i]

        for i, label in enumerate(self.resultado_labels[6:]):
            label.text = resultados_derecha[i]

class NominaApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = MainScreen(name="main")
        sm.add_widget(main_screen)
        return sm

if __name__ == "__main__":
    NominaApp().run()