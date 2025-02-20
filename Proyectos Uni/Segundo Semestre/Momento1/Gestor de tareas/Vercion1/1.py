

# Lista global para almacenar las tareas
listaTarea = []

def mostrar_tareas():
    """Muestra todas las tareas con su índice"""
    if not listaTarea:
        print("No hay tareas registradas.")
        return
    
    print("\n📌 TAREAS 📌")
    for i, tarea in enumerate(listaTarea):
        estado = "✅ Completada" if tarea["completada"] else "❌ Pendiente"
        print(f"{i}. {tarea['titulo']} - {estado} - Vence el {tarea['fecha_vencimiento']}")

def darOpcion():
    """Menú principal de la aplicación"""
    while True:
        print("\nHola, soy tu gestor de tareas. Escoge una opción:")
        print("1️⃣ Añadir una tarea")
        print("2️⃣ Editar una tarea")
        print("3️⃣ Marcar tarea como completada")
        print("4️⃣ Eliminar una tarea")
        print("5️⃣ Mostrar todas las tareas")
        print("6️⃣ Salir")
        
        opcion = input("👉 Escribe un número: ")

        if opcion == "1":
            nuevaTarea = {
                "titulo": input("Título de la tarea: "),
                "descripcion": input("Descripción: "),
                "fecha_vencimiento": input("Fecha límite (día/mes/año): "),
                "completada": False  # Al inicio, la tarea no está completada
            }
            listaTarea.append(nuevaTarea)
            print("✅ Tarea añadida con éxito.")

        elif opcion == "2":
            mostrar_tareas()
            indice = int(input("Introduce el índice de la tarea a editar: "))
            
            if 0 <= indice < len(listaTarea):
                listaTarea[indice]["titulo"] = input("Nuevo título (deja vacío para no cambiar): ") or listaTarea[indice]["titulo"]
                listaTarea[indice]["descripcion"] = input("Nueva descripción: ") or listaTarea[indice]["descripcion"]
                listaTarea[indice]["fecha_vencimiento"] = input("Nueva fecha límite: ") or listaTarea[indice]["fecha_vencimiento"]
                print("✏️ Tarea editada con éxito.")
            else:
                print("❌ Índice no válido.")

        elif opcion == "3":
            mostrar_tareas()
            indice = int(input("Introduce el índice de la tarea completada: "))
            
            if 0 <= indice < len(listaTarea):
                listaTarea[indice]["completada"] = True
                print("🎉 Tarea marcada como completada.")
            else:
                print("❌ Índice no válido.")

        elif opcion == "4":
            mostrar_tareas()
            indice = int(input("Introduce el índice de la tarea a eliminar: "))
            
            if 0 <= indice < len(listaTarea):
                listaTarea.pop(indice)
                print("🗑️ Tarea eliminada con éxito.")
            else:
                print("❌ Índice no válido.")

        elif opcion == "5":
            mostrar_tareas()

        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break  # Salir del bucle

        else:
            print("❌ Opción no válida, intenta de nuevo.")

# Iniciar el programa
darOpcion()
