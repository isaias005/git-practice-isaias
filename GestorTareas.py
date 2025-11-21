import Tarea
class GestorTareas:
    def __init__(self):
        self.tareas=[]
    def addTarea(self,nombre,estado):
        if  nombre=="":
            print("Ingrese un nombre")
        else:
            nuevaTarea=Tarea(nombre,estado)
            self.tareas.append(nuevaTarea)
    