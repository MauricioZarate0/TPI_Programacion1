from funciones import *
cabecera=["nombre","poblacion","superficie","continente"] #str,int,int,str
registro=[]

while True:
    registro = cargar_archivo(cabecera)
    print("==================================================")
    opcion=pedir_entero("1.Agregar un pais\n2.Actualizar datos de un pais\n3.Buscar pais\n4.Filtrar paises\n5.Ordenar paises\n6.Mostrar estadisticas\n7.Salir\nElija una opcion --> ",1,8)
    print("==================================================")
    match opcion:
        case 1: #Agregar pais con todos los datos necesarios
            nuevo_pais(registro,cabecera)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            print("Saliendo del programa")
            break
        case 8:
            print(registro)