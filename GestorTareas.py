from Tarea import Tarea

class GestorTareas:

    def __init__(self):

        self.tareas:list[Tarea]=[]

    def addTarea(self,nombre,estado):

        if  nombre == "":

            print("Ingrese un nombre")  
        elif  estado not in("Pendiente","Realizado"):
           
           print(" Ingrese un estado valido ")

        else:

            nuevaTarea=Tarea(nombre,estado)

            self.tareas.append(nuevaTarea)
            print("La tarea a sido anadida con exito")

    def mostrarTareas(self):

        if self.tareas==[]:

            print("La lista esta vacia")
        else:

            i = 0

            for tarea in self.tareas:
                i+=1
                print("La tarea" , i , ":" , "Su nombre es :" + tarea.get_nombre(), "La estado es :" , tarea.get_estado())
                
    def marcarTareasPorRealizar(self,pos):
        indice=pos-1
        if indice>=len(self.tareas):
            print(" La posicion esta fuera de rango , ingrese una posicion valida ")
        else:
            if(self.tareas[indice].get_estado()=="Realizado"):                    
                print(" La tarea q escogio ya estaba realizada favor de escoger otra ")

            elif self.tareas[indice].get_estado() == "Pendiente":

                     self.tareas[indice].set_estado("Realizado")

    def eliminarTarea(self,pos):

        indice=pos-1

        if indice>=len(self.tareas) or pos<0:
                  
                  print("La posicion q escogio esta fuera de rango")
        else:
         self.tareas.pop(indice)

         print("Tarea eliminada con exito")

         return
            

        

            
            

    

    