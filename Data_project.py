import pandas as pd
import random

# Función para generar datos aleatorios
def generar_datos_financieros():
    # Datos de ejemplo para generar 20 registros
    nombres = ['Ana García', 'Carlos López', 'María Rodríguez', 'Juan Martínez', 'Laura Hernández', 
           'Diego Pérez', 'Sofía González', 'Miguel Sánchez', 'Elena Díaz', 'David Ramírez',
           'Isabel Torres', 'Javier Flores', 'Carmen Ruiz', 'Alejandro Vargas', 'Patricia Castro',
           'Ricardo Morales', 'Teresa Ortega', 'Fernando Reyes', 'Lucía Mendoza', 'Gabriel Silva']
    situaciones_laborales = ['Trabajando', 'Estudiando', 'Emprendiendo', 'Desempleado']
    cuenta_ingresos_opciones = ['si', 'no']
    
    datos = []
    
    for i in range(20):
        nombre = nombres[i]
        edad = random.randint(18, 35)
        situacion_laboral = random.choice(situaciones_laborales)
        cuenta_ingresos = random.choice(cuenta_ingresos_opciones)
        
        # Si no cuenta con ingresos, las siguientes columnas deben ser 0
        if cuenta_ingresos == 'no':
            ingresos = 0
            mensualidad = 0
            beca = 0
            emprendimiento = 0
            trabajo = 0
            pasantias = 0
        else:
            # Generar ingresos realistas según la situación laboral
            if situacion_laboral == 'Estudiando':
                mensualidad = random.choice([0, 100, 150, 200])
                beca = random.choice([0, 50, 75, 100, 150])
                emprendimiento = random.choice([0, 30, 50, 80])
                trabajo = random.choice([0, 100, 200, 300])
                pasantias = random.choice([0, 200, 250, 300])
            elif situacion_laboral == 'Trabajando':
                mensualidad = 0
                beca = 0
                emprendimiento = 0
                trabajo = random.randint(800, 2000)
                pasantias = 0
            elif situacion_laboral == 'Emprendiendo':
                mensualidad = 0
                beca = 0
                emprendimiento = random.randint(500, 1500)
                trabajo = 0
                pasantias = 0
            else:  # Desempleado
                mensualidad = 0
                beca = 0
                emprendimiento = 0
                trabajo = 0
                pasantias = 0
            
            ingresos = mensualidad + beca + emprendimiento + trabajo + pasantias
        
        # Egresos fundamentales (siempre presentes)
        pasajes = random.randint(10, 20)
        comida = random.choice([8.75, 12.50, 15.25, 18.00])
        universidad = random.choice([0, 50, 100, 150])
        mascota = random.choice([0, 30, 45, 60])
        
        # Egresos ocasionales (pueden ser 0)
        helado = random.choice([0, 8, 12, 15])
        pareja = random.choice([0, 20, 35, 50])
        ropa = random.choice([0, 60, 100, 150])
        
        datos.append({
            'nombre': nombre,
            'edad': edad,
            'situacion_laboral': situacion_laboral,
            'cuenta_con_ingresos_mensuales': cuenta_ingresos,
            'ingresos': ingresos,
            'ingresos_detalle': {
                'Mensualidad': mensualidad,
                'Beca': beca,
                'Emprendimiento': emprendimiento,
                'Trabajo': trabajo,
                'Pasantias': pasantias
            },
            'egresos_fundamentales': {
                'Pasajes': pasajes,
                'Comida': comida,
                'Universidad': universidad,
                'Mascota': mascota
            },
            'egresos_ocasionales': {
                'Helado': helado,
                'Pareja': pareja,
                'Ropa': ropa
            }
        })
    
    return datos

