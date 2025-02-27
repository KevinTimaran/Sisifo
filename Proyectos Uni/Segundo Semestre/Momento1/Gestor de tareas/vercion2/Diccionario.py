Lista = []


class ListaTareas:
    def __init__(self, Titulo, Descripcion, Fecha):
        self.Titulo = Titulo
        self.Descripcion = Descripcion
        self.Fecha = Fecha

        Diccionario = {
            'Titulo': Titulo,
            'Descripcion': Descripcion,
            'fecha': Fecha
        }

        Lista.append(Diccionario)


    def MostrarTarea ():
            if not Lista:
                    print("No hay tareas registradas.")
                    
                
            print("\n📌 TAREAS 📌")
            for i, Diccionario in enumerate(Lista):
                print(f"{i}. {Diccionario['Titulo']} Vence el {Diccionario['fecha']}")



