Lista = []



def __init__(self, Titulo, Descripcion, fecha):
    self.Titulo = Titulo
    self.Descripcion = Descripcion
    self.Fecha = fecha

def darTarea (self):
    return self.Titulo

def darDescripcion (self):
    return self.Descripcion

def darFecha (self):
    return self.Fecha


Diccionario = {
    'Titulo': darTarea,
    'Descripcion': darDescripcion,
    'fecha': darFecha
}

Lista.append(Diccionario)
