from Tarea import Tarea
import json
import os

class GestorTareas:

    def __init__(self):
        self.archivo_db = "datos_tareas.json"
        self.tareas:list[Tarea]=[]
        self.cargar_datos() 
    def Guardar_datos(self):
        lista_para_json = []
        for t in self.tareas:
            # Creamos un diccionario por cada tarea
            t_dict = {
                "nombre": t.get_nombre(),
                "estado": t.get_estado()
            }
            lista_para_json.append(t_dict)
        
        try:
            with open(self.archivo_db, "w") as archivo:
                json.dump(lista_para_json, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_datos(self):
        """Lee el JSON y convierte los diccionarios de vuelta a objetos Tarea"""
        if not os.path.exists(self.archivo_db):
            return # Si el archivo no existe, no hacemos nada (la lista sigue vacía)

        try:
            with open(self.archivo_db, "r") as archivo:
                datos = json.load(archivo) # Esto carga una lista de diccionarios
                
                self.tareas = [] # Limpiamos por seguridad
                for d in datos:
                    # Reconstruimos el objeto Tarea
                    nueva_tarea = Tarea(d["nombre"], d["estado"])
                    self.tareas.append(nueva_tarea)
        except Exception as e:
            print(f"Error al cargar datos o archivo corrupto: {e}")
            self.tareas = []

    def addTarea(self,nombre,estado):

        if  nombre == "":

            print("Ingrese un nombre")  
        elif  estado not in("Pendiente","Realizado"):
           
           print(" Ingrese un estado valido ")

        else:

            nuevaTarea=Tarea(nombre,estado)

            self.tareas.append(nuevaTarea)
            self.Guardar_datos()
            print("La tarea a sido guarda en la base de datos ")
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
                     self.Guardar_datos()
                     print("Los datos han sido actualizados con exito ")

    def eliminarTarea(self,pos):

        indice=pos-1

        if indice>=len(self.tareas) or pos<0:
                  
                  print("La posicion q escogio esta fuera de rango")
        else:
         self.tareas.pop(indice)
         self.Guardar_datos()
         print(" Tarea eliminada con exito y cambios guardados ")

         return
            

        

            
            

    

    