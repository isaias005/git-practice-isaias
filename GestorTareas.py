import Tarea
class GestorTareas:

    def __init__(self):

        self.tareas=[]

    def addTarea(self,nombre,estado):

        if  nombre == "":

            print("Ingrese un nombre")  
        elif  not estado=="Pendiente"or"Realizado":
           
           print(" Ingrese un estado valido ")

        else:

            nuevaTarea=Tarea(nombre,estado)

            self.tareas.append(nuevaTarea)

    def mostarTareas(self):

        if self.tareas==[]:

            print("La lista esta vacia")
        else:

            i = 0

            for tarea in self.tareas:

                print("La tarea" + i++ + ":" + "Su nombre es :" + tarea.get_nombre() + "La estado es :" + tarea.get_estado())
                
    def marcarTareasPorRealizar(self,pos):

      if pos>len(self.tareas):
          
          print(" La posicion esta fuera de rango , ingrese una posicion valida ")

      else:
          
          for a in range(pos):
              
              if a==pos:

                if(self.tareas[a].get_esatdo()=="Realizado"):
                      
                      print(" La tarea q escogio ya estaba realizada favor de escoger otra ")

                elif self.tareas[a].get_estadp() == "Pendiente":

                    self.tareas[a].get_estado() == "Realizado "   
    def eliminarTarea(self,pos):

        for a in range(pos):

            if a==pos:
             
             self.tareas.remove(a)
            

        

            
            

    

    