from Conversion import Conversion
#Uso try y axcept para detectar un error relacionado con la entra de de letras y no numeros 
try:
    #Preguntas para el usuario
    Litrosleche = float(input("Ingrese la cantidad de leche en litros: "))
    PrecioLeche = float(input("Ingrese en precio que se cobrara por litro de leche: "))
    
    
    main = Conversion(Litrosleche, PrecioLeche)
    totalGalosnes = main.darConversion()
    totalPrecio = main.darPrecio()

    if totalGalosnes is not None:
        print(f"""En {main.darLitros()} litros hay {totalGalosnes:.3f} galones y se cobrara un total de {totalPrecio:.0f}""")

except ValueError:
    print("Por favor digite un numero valido")

