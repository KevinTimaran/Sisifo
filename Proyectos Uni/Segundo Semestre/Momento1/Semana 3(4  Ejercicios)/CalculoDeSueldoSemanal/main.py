from CalcularHoras import HorasSemana

try:
    Hora = float(input("Digite las horas que ha trabajado en la semana: "))
    Pago = float(input("Digite el pago que recibe en una hora de trabajo: "))
    
    main= HorasSemana(Hora, Pago)
    toltal = main.CalcularSueldo()

    print (f"""Su pago por trabajar {main.darHora()} horas en la semana es de {toltal}.""")
    
except ValueError:
    print("Por favor ingrese un numero valido.")