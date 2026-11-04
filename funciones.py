import csv
#FUNCIONES
continentes=("Africa","America","Antartida","Asia","Europa","Oceania")

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
        entrada = input(mensaje).strip()
        if entrada=="":
            print("Error, ingrese algo.")
            if persiste==False:
                return
        else:
            return entrada

def cargar_archivo(cabecera): #Cargar elementos del archivo en la variable
    registro_nuevo = []
    try:
        with open("archivo.csv","r",newline="",encoding="utf-8") as archivo:
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
        with open("archivo.csv","w",newline="",encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=cabecera)
            escritor.writeheader()
        return registro_nuevo

def comparar_pais(pais):
    with open("lista_paises.txt","r",encoding="utf-8") as archivo:
        for filas in archivo:
            filas=filas.strip()
            if pais==filas:
                print("El pais ingresado coincide con el registro de la ONU.")
                return pais
        print("El pais ingresado no existe o no coincide con los registros de la ONU.")
        return None
#MENU

#1
def nuevo_pais(registro,cabecera): #Agregar un pais
    nuevo_registro = registro
    nombre = pedir_cadena("Ingrese el nombre del pais nuevo (respetar tildes): ",persiste=False).title()
    nombre = comparar_pais(nombre) #Comparo el nombre con el registro oficial para ver si el pais existe
    if nombre==None:
        return
    for paises in nuevo_registro: #Buscar si el pais ya esta registrado
        if paises["nombre"]==nombre:
            print("Este pais ya esta registrado, si quiere actualizar sus datos use la opcion 2.")
            return
    poblacion = pedir_entero("Ingrese la poblacion: ",0,persiste=False)
    superficie = pedir_entero("Ingrese la superficie del pais (km2): ",0,persiste=False)
    continente = pedir_cadena("Ingrese el continente de este pais: ",persiste=False).title()
    if not continente in continentes: #Verificar que el continente sea real
        print("Error, ingrese un continente valido.")
        return
    
    if nombre==None or poblacion==None or superficie==None or continente==None: #None es la devolucion cuando ocurre un error
        return
    
    pais = {"nombre":nombre,"poblacion":poblacion,"superficie":superficie,"continente":continente} #Creo el diccionario para guardar el pais
    nuevo_registro.append(pais)
    
    try:
        with open("archivo.csv","w",newline="",encoding="utf-8") as archivo: #Abro el archivo para volcar todos los paises a la misma vez
            escritor=csv.DictWriter(archivo,fieldnames=cabecera)
            escritor.writeheader()
            escritor.writerows(nuevo_registro)
            print("Se cargo el pais correctamente")
            return
    except PermissionError:
        print("Error, el archivo de guardado esta siendo utilizado, cierrelo y reintente")


