INFORME DE CONCEPTOS APLICADOS
En este trabajo practico final integrador se uso la mayor parte de los conocimientos teoricos y practicos aprendidos en programacion I, si bien no abarca las ultimas unidades, engloba de forma general todo el conocimiento necesario para llevar a cabo la creacion base de una aplicacion, a continuacion se definiran todas las estructuras usadas y aplicadas en el mismo.
-------------------------------------------
o Listas: Es una estructura de datos que usa [] para identificarse, es ordenada, mutable, permite guardar valores y usa como separacion de sus elementos las , (coma simple) .
Ejemplo de lista: [manzana,zanahoria,5,sandia]
Algunas funciones utilizadas para el manejo de listas son:
lista.index(valor) : Obtiene el indice en el que se encuentra el valor ingresado, da error si el valor no existe.
lista.append(valor) : Agrega un elemento al final de la lista.
lista.pop(indice) : Elimina por posicion dada y retorna el valor encontrado en esa posicion.
lista.remove(valor) : Elimina la primer coincidencia encontrada en la lista .
-------------------------------------------
o Diccionarios: Es una estructura de datos de la forma clave-valor, mutable y ordenada. Usa como separacion de sus elementos las , (coma simple)
Ejemplo de diccionario: {nombre:Mauricio,apellido:Zarate,edad:25,ciudad:Mendoza}
Algunas funciones utilizadas para el manejo de diccionarios son:
diccionario.upgrade({[clave]:valor}) : Agrega un elemento al diccionario
-------------------------------------------
o Funciones: Son bloques de codigo reutilizables y accesibles atravez de un nombre definido.
Ejemplo: def nombre(numero1,numero2): #nombre y parametros a utilizar
            valor= numero1 + numero2 #lineas de codigo a ejecutar
            return valor #Llamado para finalizar la funcion y devolver un valor
-------------------------------------------
o Condicionales: Segmentos de codigo que se ejecutaran solo si pasan por un filtro, basado en condiciones especificas, su estructura es if-elif-else.
Ejemplo: Solo ejecutaria el segmente else.
numero=5
if numero>5: #Si el numero es mayor a 5.
    print("Es mayor a 5")
elif numero<5: #Sino si el numero es menor a 5.
    print("Es menor a 5")
else: #Si no cumple ninguna de las condiciones anteriores entonces.
    print("Es igual a 5")
-------------------------------------------
o Ordenamientos: En estructuras de datos son datos por indices o por valores de coincidencia.
Tambien hay funciones aplicables que siguen ciertos formatos para encontrar valores coincidentes y ordenarlos de alguna forma establecida.
Metodos de ordenamiento:
sort() : Modifica una estructura de datos usando de referencia el codigo ASCCI para ordenarla
sorted() : Parecida a la anterior pero no modifica la variable original.
-------------------------------------------
o Estadísticas básicas: 
-------------------------------------------
o Archivos CSV: Es un formato de archivo de texto, que usa un ordenamiento tipo fila-columna, cada valor separado por una , (coma) es una columna y las filas son dadas por los saltos de linea.
-------------------------------------------
• Definir el flujo de operaciones principales en un diagrama o esquema: 

-------------------------------------------
Problemas durante la programacion:
-Funcion nuevo_pais(): linea 109 ->No encontraba la forma de añadir un elemento al final de la lista del csv. ya que con el metodo "w" se sobreescribia y con "a" no encontraba la forma de hacer un salto de linea con el escritor, la solucion que encontre fue sobreescribir el archivo y volcar la variable de registro sobre el archivo con la funcion cargar_archivo()