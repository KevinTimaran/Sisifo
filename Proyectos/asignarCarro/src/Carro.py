class autos:
    def __init__(self, Marca, Placa, PesoMaximo: int, ):
        self.Marca = Marca
        self.Placa = Placa
        self.PesoMaximo = PesoMaximo
        

    def __str__(self): return f"Marca: {self.Marca}, Placa: {self.Placa}, Peso Máximo: {self.PesoMaximo} kg,"
   



Carro1 = autos ("Toyota", "GHy778", 80,  )
Carro2 = autos("Kia", "TOD50", 50,  )
Carro3 = autos("Masda", "POL48", 40, )
Carro4 = autos("ferri", "OPF69", 35, )






