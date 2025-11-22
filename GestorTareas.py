import Tarea
class GestorTareas:

    def __init__(self):

        self.tareas=[]

    def addTarea(self,nombre,estado):

        if  nombre == "":

            print("Ingrese un nombre")  

        else:

            nuevaTarea=Tarea(nombre,estado)

            self.tareas.append(nuevaTarea)
            
    def mostarTareas(self):

        if self.tareas==[]:

            print("La lista esta vacia")
        else:

            i = 0

            for tarea in self.tareas:

                print("La tarea" + i++ + ":" + "Su nombre es :" + tarea.get_nombre + "La estado es :" + tarea.get_estado)


    