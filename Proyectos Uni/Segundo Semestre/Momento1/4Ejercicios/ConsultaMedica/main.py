from ConsultaMedica import calcularCosto  


try:
    # Pedir al usuario el número de cita
    numeroCita = int(input("Ingrese el número de su cita: "))

    
    costoActual, totaAcumulado = calcularCosto(numeroCita)

    # Mostrar los resultados
    print(f"Costo de la cita actual: ${costoActual:,}")
    print(f"Total pagado hasta la fecha: ${totaAcumulado:,}")

except ValueError:
    print("Por favor digite un numero valido")
