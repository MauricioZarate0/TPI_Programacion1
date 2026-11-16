import csv
#FUNCIONES
continentes=("Africa","America","Antartida","Asia","Europa","Oceania")
direccion_archivo="paises.csv"

def pedir_entero(mensaje,minimo=None,maximo=None,persiste=True):
    while True:
        try:
            entrada = int(input(mensaje).strip())
            if entrada=="":
                print("Error, ingrese algo.")
                if persiste==False:
                    return
                
            if minimo is not None and entrada<minimo:
                print(f"Error,el valor debe ser mayor a {minimo}.")
                if persiste==False:
                    return
            elif maximo is not None and entrada>maximo:
                print(f"Error,el valor debe ser mayor a {maximo}.")
                if persiste==False:
                    return
            else:
                return entrada
        except ValueError:
            print("Error, ingrese un numero.")

def pedir_cadena(mensaje,persiste=True):
    while True:
        entrada = input(mensaje).strip().title()
        if entrada=="":
            print("Error, ingrese algo.")
            if persiste==False:
                return None
        else:
            return entrada

def cargar_archivo(cabecera): #Cargar elementos del archivo en la variable
    registro_nuevo = []
    try:
        with open(direccion_archivo,"r",newline="",encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo,fieldnames=cabecera) #cabecera=["nombre","poblacion","superficie","continente"]
            next(lector) #Salto la primer linea que es el nombre de las columnas
        
            for lineas in lector: #Recorro linea a linea
                try: #Por si se detecta alguna linea con datos erroneos, en este caso se saltara la linea con next()
                    nombre = (lineas["nombre"]).title()
                    poblacion = int(lineas["poblacion"])
                    superficie = int(lineas["superficie"])
                    continente = (lineas["continente"]).title()
                    if not continente in continentes: #corroborar que los continentes coincidan con los validos
                        next(lector)
                    pais={"nombre":nombre,"poblacion":poblacion,"superficie":superficie,"continente":continente}
                    registro_nuevo.append(pais)
                except ValueError: #Errores al intentar volver int las variables
                    continue
                except TypeError:
                    continue
        return registro_nuevo
    except FileNotFoundError: #Si no se encuentra el archivo, lo creamos y dejamos escrito el nombre de las columnas
        print("No se encontro un archivo guardado localmente.")
        with open(direccion_archivo,"w",newline="",encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=cabecera)
            escritor.writeheader()
        return registro_nuevo

def cargar_registro(registro,cabecera): #Cargar elemento de la variable al archivo
    with open(direccion_archivo,"w",newline="",encoding="utf-8") as archivo:
        escritor=csv.DictWriter(archivo,fieldnames=cabecera)
        escritor.writeheader()
        escritor.writerows(registro)

def comparar_pais(pais): #Acceso al .txt con los paises registrados por la ONU
    with open("lista_paises.txt","r",encoding="utf-8") as archivo:
        for filas in archivo: #Recorro el archivo buscando la coincidencia
            filas=filas.strip() #Eliminar los saltos de linea
            if pais==filas:
                print("El pais ingresado coincide con el registro de la ONU.")
                return pais
        print("El pais ingresado no existe o no coincide con los registros de la ONU.")
        return None
#MENU

#1
def nuevo_pais(registro,cabecera): #Agregar un pais
    nuevo_registro = registro
    nombre = pedir_cadena("Ingrese el nombre del pais nuevo (respetar tildes): ",persiste=False)
    nombre = comparar_pais(nombre) #Comparo el nombre con el registro oficial para ver si el pais existe
    if nombre==None:
        return
    for paises in nuevo_registro: #Buscar si el pais ya esta registrado
        if paises["nombre"]==nombre:
            print("Este pais ya esta registrado, si quiere actualizar sus datos use la opcion 2.")
            return
    poblacion = pedir_entero("Ingrese la poblacion: ",0,persiste=False)
    superficie = pedir_entero("Ingrese la superficie del pais (km2): ",0,persiste=False)
    continente = pedir_cadena("Ingrese el continente de este pais: ",persiste=False)
    if not continente in continentes: #Verificar que el continente sea real
        print("Error, ingrese un continente valido.")
        return
    
    if nombre==None or poblacion==None or superficie==None or continente==None: #None es la devolucion cuando ocurre un error
        return
    
    pais = {"nombre":nombre,"poblacion":poblacion,"superficie":superficie,"continente":continente} #Creo el diccionario para guardar el pais
    nuevo_registro.append(pais)
    
    try:
        cargar_registro(nuevo_registro,cabecera)
        print("Se cargo el pais correctamente")
        return
    except PermissionError:
        print("Error, el archivo de guardado esta siendo utilizado, cierrelo y reintente")

def actualizar_datos(registro,cabecera): #Actualizar poblacion y superficie de un pais
    registro_nuevo=registro
    print("=== Actualizacion de datos ===")
    nombre=pedir_cadena("Ingrese el nombre del pais (respete tildes): ",False)
    if nombre==None: #None = error
        return
    
    for lineas in registro_nuevo: #Recorro el registro buscando que el pais este registrado
        if lineas["nombre"]==nombre: #Una vez localizado, reemplazo poblacion y superficie por las nuevas ingresadas
            poblacion=pedir_entero("Ingrese la nueva poblacion: ",0,persiste=True)
            superficie=pedir_entero("Ingrese la nueva superficie (km2): ",0,persiste=True)
            lineas["poblacion"]=poblacion
            lineas["superficie"]=superficie
            cargar_registro(registro_nuevo,cabecera)
            return
    print("No se encontro registrado el pais, use la opcion 1 si desea agregarlo al registro") #Si nose encuentra al pais en el registro se devuelve al menu
    return

def buscar_pais(registro): #Buscar un pais o paises por coincidencia parcial o total
    nombre=pedir_cadena("Ingrese el nombre del pais que desea buscar (respete tildes): ",False)
    if nombre==None: #None=error
        return

    coincidencias=[]
    for pais in registro: #recorro el registro buscando el texto ingresado
        nombre_registro=pais["nombre"]
        if nombre in nombre_registro: #Verifico que el texto ingresado sea igual al nombre o parcialmente igual y lo agrego a las coincidencias
            coincidencias.append(pais)

    if len(coincidencias)==0: #Si no hay coincidencias se sale de la funcion
        print("No se encontraron coincidencias.")
        return
    else:
        print("=== COINCIDENCIAS ===") #Muestro las coincidencias
        for pais in coincidencias:
            print(f"Pais: {pais["nombre"]} - Poblacion: {pais["poblacion"]} - Superficie: {pais["superficie"]} - Continente: {pais["continente"]}")
        return

def filtrar_paises(registro): #Filtro de paises por continente,poblacion,superficie
    opcion = input("a.Filtro por continente\nb.Filtro por rango de poblacion\nc.Filtro por rango de superficie\nElija una opcion para continuar -->")
    match opcion:
        case "a": #Por continente
            continente=pedir_cadena("Ingrese el continente para filtrar los paises: ",False)
            if continente==None:
                return
            if continente in continentes: #Recorro el registro de paises y me quedo con aquellos que coincidan con el continente
                print(f"=== PAISES DE {(continente).upper()} ===")
                for paises in registro:
                    if paises["continente"]==continente:
                        print(f"Pais: {paises["nombre"]} - Poblacion: {paises["poblacion"]} - Superficie: {paises["superficie"]}")
                return
            else:
                print("Error, ingrese un continente real.")
                return
        case "b": #Por poblacion
            minimo = pedir_entero("Ingrese el rango minimo de poblacion: ",-1,persiste=False)
            maximo= pedir_entero("Ingrese el rango maximo de poblacion: ",-1,persiste=False)
            if minimo==None or maximo==None:
                return
            if minimo>maximo:
                print("El minimo debe ser inferior al maximo")
                return
            print(f"== Lista de paises con poblacion entre {minimo}-{maximo} ==") #Comparo y imprimo aquellos que superen el minimo pero sean inferiores al maximo
            for paises in registro:
                if paises["poblacion"]>=minimo and paises["poblacion"]<=maximo:
                    print(f"Pais: {paises["nombre"]} - Poblacion: {paises["poblacion"]} - Superficie: {paises["superficie"]} - Continente: {paises["continente"]}")
            return
        case "c": #por superficie
            minimo = pedir_entero("Ingrese el rango minimo de superficie (km2): ",-1,persiste=False)
            maximo= pedir_entero("Ingrese el rango maximo de superficie (km2): ",-1,persiste=False)
            if minimo==None or maximo==None:
                return
            if minimo>maximo:
                print("El minimo debe ser inferior al maximo")
                return
            print(f"== Lista de paises con superficie entre {minimo}-{maximo} ==") #Comparo y imprimo aquellos que superen el minimo pero sean inferiores al maximo
            for paises in registro:
                if paises["superficie"]>=minimo and paises["superficie"]<=maximo:
                    print(f"Pais: {paises["nombre"]} - Poblacion: {paises["poblacion"]} - Superficie: {paises["superficie"]} - Continente: {paises["continente"]}")
            return
        case _:
            print("Error, elija una opcion valida.")
            return

def ordenar_paises(registro): #Organizar paises por nombre,poblacion,superficie
    registro_nuevo = registro
    opcion=input("a.Organizar por nombre\nb.Organizar por poblacion\nc.Organizar por superficie\nElija una opcion para continuar --> ").lower()
    match opcion:
        case "a": #Por nombre - Ordenar la lista usando la llave "nombre"
            opcion_orden=input("Desea que este ordenado de forma:\n1.Ascendente\n2.Descendente\nElija una opcion --> ")
            match opcion_orden:
                case "1": #Ascendente
                    registro_ordenado = sorted(registro, key=lambda p: p["nombre"]) 
                    for pais in registro_ordenado:
                        print(f"Pais: {pais["nombre"]} - Poblacion: {pais["poblacion"]} - Superficie: {pais["superficie"]} - Continente: {pais["continente"]}")
                case "2": #Descendente
                    registro_ordenado = sorted(registro, key=lambda p: p["nombre"],reverse=True) 
                    for pais in registro_ordenado:
                        print(f"Pais: {pais["nombre"]} - Poblacion: {pais["poblacion"]} - Superficie: {pais["superficie"]} - Continente: {pais["continente"]}")
                case _:
                    print("Error, elija una de las dos formas.")
                    return
        case "b": #Por poblacion - Ordenar la lista usando la llave "poblacion"
            opcion_orden=input("Desea que este ordenado de forma:\n1.Ascendente\n2.Descendente\nElija una opcion --> ")
            match opcion_orden:
                case "1": #Ascendente
                    registro_ordenado = sorted(registro, key=lambda p: p["poblacion"]) 
                    for pais in registro_ordenado:
                        print(f"Pais: {pais["nombre"]} - Poblacion: {pais["poblacion"]} - Superficie: {pais["superficie"]} - Continente: {pais["continente"]}")
                case "2": #Descendente
                    registro_ordenado = sorted(registro, key=lambda p: p["superficie"],reverse=True) 
                    for pais in registro_ordenado:
                        print(f"Pais: {pais["nombre"]} - Poblacion: {pais["poblacion"]} - Superficie: {pais["superficie"]} - Continente: {pais["continente"]}")
                case _:
                    print("Error, elija una de las dos formas.")
                    return
        case "c": #Por superficie - Ordenar la lista usando la llave "superficie"
            opcion_orden=input("Desea que este ordenado de forma:\n1.Ascendente\n2.Descendente\nElija una opcion --> ")
            match opcion_orden:
                case "1": #Ascendente
                    registro_ordenado = sorted(registro, key=lambda p: p["superficie"]) #Ordenar la lista usando la llave "superficie"
                    for pais in registro_ordenado:
                        print(f"Pais: {pais["nombre"]} - Poblacion: {pais["poblacion"]} - Superficie: {pais["superficie"]} - Continente: {pais["continente"]}")
                case "2": #Descendente
                    registro_ordenado = sorted(registro, key=lambda p: p["superficie"],reverse=True) #Ordenar la lista usando la llave "superficie"
                    for pais in registro_ordenado:
                        print(f"Pais: {pais["nombre"]} - Poblacion: {pais["poblacion"]} - Superficie: {pais["superficie"]} - Continente: {pais["continente"]}")
                case _:
                    print("Error, elija una de las dos formas.")
                    return
        case _:
            print("Error, elija una opcion valida.")
            return

def mostrar_estadisticas(registro): #País con mayor y menor población - Promedio de población - Promedio de superficie - Cantidad de países por continente
    print("==== ESTADISTICAS ====")
    menu = input("1.Pais con mayor y menor poblacion\n2.Promedio de poblacion\n3.Promedio de superficie\n4.Cantidad de paises por continente\nElija una opcion --> ")
    match menu:
        case "1": #Pais con mayor y menor poblacion
            registro_ordenado=sorted(registro,key=lambda p:p["poblacion"]) #Ordeno y acceso al numero de poblacion mas bajo y al mas alto mediante indice
            print(f"Pais con menor poblacion: Pais: {registro_ordenado[0]["nombre"]} - Poblacion: {registro_ordenado[0]["poblacion"]} - Superficie: {registro_ordenado[0]["superficie"]} - Continente: {registro_ordenado[0]["continente"]}")
            print(f"Pais con mayor poblacion: Pais: {registro_ordenado[-1]["nombre"]} - Poblacion: {registro_ordenado[-1]["poblacion"]} - Superficie: {registro_ordenado[-1]["superficie"]} - Continente: {registro_ordenado[-1]["continente"]}")
        case "2": #Promedio de poblacion
            sumatoria=0
            for pais in registro: #Recorro todos los paises agregando la variable poblacion a la sumatoria
                poblacion = int(pais["poblacion"])
                sumatoria+=poblacion
            promedio_poblacion=sumatoria/len(registro)

            print("=== PROMEDIO POBLACION ===")
            print(f"El promedio de poblacion entre estos {len(registro)} paises es de: {(promedio_poblacion):.2f} habitantes")
        case "3": #Promedio de superficie
            sumatoria=0
            for pais in registro: #Misma logica que para el case 2
                superficie = int(pais["superficie"])
                sumatoria+=superficie
            promedio_superficie=sumatoria/len(registro)
            
            print("=== PROMEDIO SUPERFICIE ===")
            print(f"El promedio de superficie entre estos {len(registro)} paises es de: {(promedio_superficie):.2f} km2")
        case "4": #Cantidad de paises por continente
            registro_ordenado=sorted(registro,key=lambda p:p["continente"]) #Ordeno aunque daria igual porque recorro todos los valores
            conteo=[]
            for continente in continentes: #Para cada continente recorro la lista buscando quien presenta el mismo continente que el recorrido actualmente
                contador=0
                for pais in registro_ordenado:
                    if continente==pais["continente"]: #Si el continente coincide lo sumo al contador
                        contador +=1
                conteo.append(contador) #Termino de recorrer todos los paises con el continente actual guardardo el contador y saltando al siguiente continente

            print("=== PAISES POR CONTINENTE ===")
            for i in range(len(continentes)):
                print(f"{continentes[i]}: {conteo[i]} paises")
        case _:
            print("Error, reintente eligiendo una de las opciones validas")
            return