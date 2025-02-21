
def calcularCosto(numeroCita):


    #Parte del cidigi cirve para Validar que el número de cita sea mayor o igual a 1
    if numeroCita < 1:
        raise ValueError("El número de cita debe ser 1 o mayor.")
    
    # Se define la cita segun el numero de citas
    if numeroCita <= 3:
        costoActual = 200000
    elif numeroCita <= 5:
        costoActual = 150000
    elif numeroCita <= 8:
        costoActual = 100000
    else:
        costoActual = 50000

    # Calcular el total acumulado sumando el costo de todas las citas anteriores
    totaAcumulado = 0
    for cita in range(1, numeroCita + 1):
        if cita <= 3:
            totaAcumulado += 200000
        elif cita <= 5:
            totaAcumulado += 150000
        elif cita <= 8:
           totaAcumulado += 100000
        else:
            totaAcumulado += 50000

    return costoActual, totaAcumulado






        
    


