from GestorTareas import GestorTareas
import os
def main() : 
 salir=False  
 g=GestorTareas()
 g.addTarea("Recoger mandados","Pendiente")
 g.addTarea("Arreglar Mesa","Pendiente")
 g.addTarea("Arreglar Silla","Pendiente")
 g.addTarea("Leer libro","Realizado")
 g.addTarea("Correr maraton","Realizado")
 g.addTarea("Tener sexo","Pendiente")
 while salir == False:
     print("Gestor de tareas")
     print("1-Mostar lista de tareas ")
     print("2-anadir tarea ")
     print("3-marcar tarea como realizada ")
     print("4-eliminar tarea ")
     print("5-salir ")
     eleccion=int(input("Escoja una opcion "))
     os.system('cls')
     if eleccion==1:
        g.mostrarTareas()
        input("Volver...")
        os.system('cls')
     elif eleccion==2:
        nombre=str(input("Ingrese el nombre de la tarea:"))
        estado=str(input("Ingrese el estado de la tarea:"))
        g.addTarea(nombre,estado)
        input("Volver...")
        os.system('cls')
     elif eleccion==3:
        g.mostrarTareas()
        marcar=int(input("Escoja la tarea que desee realizar: "))
        g.marcarTareasPorRealizar(marcar)
        input("Volver...")
        os.system('cls')
     elif eleccion==4:
        g.mostrarTareas()
        eliminar=int(input("Escoja una tarea que quiera eliminar:"))
        g.eliminarTarea(eliminar)
        input("Volver...")
        os.system('cls')
     elif eleccion==5:
        print("Usted a cerrado el programa ")
        print("El programa a sido cerrado con exito... ")
        salir=True
        input("Volver...")
        os.system('cls')
     else:
        print("Opcion no valida , por favor escoja correctamente una de las opciones")
if __name__=="__main__":
    main()