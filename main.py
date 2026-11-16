from funciones import *
cabecera=["nombre","poblacion","superficie","continente"] #str,int,int,str

while True:
    registro = cargar_archivo(cabecera)
    print("==================================================")
    opcion=pedir_entero("1.Agregar un pais\n2.Actualizar datos de un pais\n3.Buscar pais\n4.Filtrar paises\n5.Ordenar paises\n6.Mostrar estadisticas\n7.Salir\nElija una opcion --> ",1,7)
    print("==================================================")
    match opcion:
        case 1: #Agregar pais con todos los datos necesarios
            nuevo_pais(registro,cabecera)
        case 2: #Actualizar datos de poblacion y superficie de un pais
            actualizar_datos(registro,cabecera)
        case 3: #Buscar pais por coincidencia o nombre completo
            buscar_pais(registro)
        case 4: #Segun la opcion clasificara y mostrara solo los elementos que cumplan una condicion
            filtrar_paises(registro)
        case 5: #Ordenar la lista de paises de una determinada forma
            ordenar_paises(registro)
        case 6: #Mostrar estadisticas recolectadas entre la sumatoria de paises
            mostrar_estadisticas(registro)
        case 7:
            print("Saliendo del programa")
            break