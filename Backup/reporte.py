from nomina import calcular_sueldo

def reporte(empleados):
    print('Sueldos de los empleados')
    for empleado in empleados:
        sueldo_final=calcular_sueldo(empleado['hora'],empleado['valor'])
        print(f"Nombre: {empleado["nombre"]} - Su sueldo:${sueldo_final}")