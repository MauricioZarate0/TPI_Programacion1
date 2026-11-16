# TPI_Programacion1

## Funciones del menú: ejemplos de entrada y salida

Para iniciar el programa:

```
python main.py
```

Menú principal:

```
1.Agregar un pais
2.Actualizar datos de un pais
3.Buscar pais
4.Filtrar paises
5.Ordenar paises
6.Mostrar estadisticas
7.Salir
Elija una opcion -->
```

Los ejemplos usan el dataset base de `paises.csv`.

---

### 1. Agregar un país

Pide el nombre, la población, la superficie (km²) y el continente. El nombre se compara con `lista_paises.txt` (países reconocidos por la ONU). El país se guarda en `paises.csv`.

**Caso correcto**

```
Ingrese el nombre del pais nuevo (respetar tildes): Japón
El pais ingresado coincide con el registro de la ONU.
Ingrese la poblacion: 125800000
Ingrese la superficie del pais (km2): 377975
Ingrese el continente de este pais: Asia
Se cargo el pais correctamente
```

**País ya registrado**

```
Ingrese el nombre del pais nuevo (respetar tildes): Argentina
El pais ingresado coincide con el registro de la ONU.
Este pais ya esta registrado, si quiere actualizar sus datos use la opcion 2.
```

**País inexistente**

```
Ingrese el nombre del pais nuevo (respetar tildes): Wakanda
El pais ingresado no existe o no coincide con los registros de la ONU.
```

---

### 2. Actualizar datos de un país

Reemplaza la población y la superficie de un país ya registrado.

**Caso correcto**

```
=== Actualizacion de datos ===
Ingrese el nombre del pais (respete tildes): Argentina
Ingrese la nueva poblacion: 46700000
Ingrese la nueva superficie (km2): 2780400
```

El archivo `paises.csv` queda con `Argentina,46700000,2780400,America`.

**País no registrado**

```
=== Actualizacion de datos ===
Ingrese el nombre del pais (respete tildes): Chile
No se encontro registrado el pais, use la opcion 1 si desea agregarlo al registro
```

---

### 3. Buscar país

Busca por coincidencia parcial o exacta del nombre.

**Coincidencia parcial**

```
Ingrese el nombre del pais que desea buscar (respete tildes): Arg
=== COINCIDENCIAS ===
Pais: Argentina - Poblacion: 46654581 - Superficie: 2780400 - Continente: America
Pais: Argelia - Poblacion: 45606480 - Superficie: 2381741 - Continente: Africa
```

**Sin resultados**

```
Ingrese el nombre del pais que desea buscar (respete tildes): Chile
No se encontraron coincidencias.
```

---

### 4. Filtrar países

Submenú:

```
a.Filtro por continente
b.Filtro por rango de poblacion
c.Filtro por rango de superficie
```

**a. Por continente**

```
Ingrese el continente para filtrar los paises: America
=== PAISES DE AMERICA ===
Pais: Brasil - Poblacion: 216422446 - Superficie: 8515767
Pais: Argentina - Poblacion: 46654581 - Superficie: 2780400
Pais: Estados Unidos - Poblacion: 334914895 - Superficie: 9833520
Pais: Costa Rica - Poblacion: 5212173 - Superficie: 51100
Pais: República Dominicana - Poblacion: 11332972 - Superficie: 48671
```

**b. Por rango de población**

```
Ingrese el rango minimo de poblacion: 10000000
Ingrese el rango maximo de poblacion: 50000000
== Lista de paises con poblacion entre 10000000-50000000 ==
Pais: Australia - Poblacion: 26638544 - Superficie: 7692024 - Continente: Oceania
Pais: Argentina - Poblacion: 46654581 - Superficie: 2780400 - Continente: America
Pais: Afganistán - Poblacion: 41128771 - Superficie: 652230 - Continente: Asia
Pais: Argelia - Poblacion: 45606480 - Superficie: 2381741 - Continente: Africa
Pais: República Dominicana - Poblacion: 11332972 - Superficie: 48671 - Continente: America
```

**c. Por rango de superficie**

```
Ingrese el rango minimo de superficie (km2): 1000000
Ingrese el rango maximo de superficie (km2): 8000000
== Lista de paises con superficie entre 1000000-8000000 ==
Pais: Australia - Poblacion: 26638544 - Superficie: 7692024 - Continente: Oceania
Pais: Argentina - Poblacion: 46654581 - Superficie: 2780400 - Continente: America
Pais: Argelia - Poblacion: 45606480 - Superficie: 2381741 - Continente: Africa
```

**Rango inválido**

```
Ingrese el rango minimo de superficie (km2): 500
Ingrese el rango maximo de superficie (km2): 100
El minimo debe ser inferior al maximo
```

---

### 5. Ordenar países

Submenú: `a` por nombre, `b` por población, `c` por superficie. Después pide `1` (ascendente) o `2` (descendente).

**Por nombre, ascendente (a → 1)**

```
Pais: Afganistán - Poblacion: 41128771 - Superficie: 652230 - Continente: Asia
Pais: Argelia - Poblacion: 45606480 - Superficie: 2381741 - Continente: Africa
Pais: Argentina - Poblacion: 46654581 - Superficie: 2780400 - Continente: America
Pais: Australia - Poblacion: 26638544 - Superficie: 7692024 - Continente: Oceania
Pais: Brasil - Poblacion: 216422446 - Superficie: 8515767 - Continente: America
Pais: Costa Rica - Poblacion: 5212173 - Superficie: 51100 - Continente: America
Pais: Estados Unidos - Poblacion: 334914895 - Superficie: 9833520 - Continente: America
Pais: República Dominicana - Poblacion: 11332972 - Superficie: 48671 - Continente: America
```

**Por superficie, descendente (c → 2)**

```
Pais: Estados Unidos - Poblacion: 334914895 - Superficie: 9833520 - Continente: America
Pais: Brasil - Poblacion: 216422446 - Superficie: 8515767 - Continente: America
Pais: Australia - Poblacion: 26638544 - Superficie: 7692024 - Continente: Oceania
Pais: Argentina - Poblacion: 46654581 - Superficie: 2780400 - Continente: America
Pais: Argelia - Poblacion: 45606480 - Superficie: 2381741 - Continente: Africa
Pais: Afganistán - Poblacion: 41128771 - Superficie: 652230 - Continente: Asia
Pais: Costa Rica - Poblacion: 5212173 - Superficie: 51100 - Continente: America
Pais: República Dominicana - Poblacion: 11332972 - Superficie: 48671 - Continente: America
```

---

### 6. Mostrar estadísticas

Submenú:

```
1.Pais con mayor y menor poblacion
2.Promedio de poblacion
3.Promedio de superficie
4.Cantidad de paises por continente
```

**1. Mayor y menor población**

```
Pais con menor poblacion: Pais: Costa Rica - Poblacion: 5212173 - Superficie: 51100 - Continente: America
Pais con mayor poblacion: Pais: Estados Unidos - Poblacion: 334914895 - Superficie: 9833520 - Continente: America
```

**2. Promedio de población**

```
=== PROMEDIO POBLACION ===
El promedio de poblacion entre estos 8 paises es de: 90988857.75 habitantes
```

**3. Promedio de superficie**

```
=== PROMEDIO SUPERFICIE ===
El promedio de superficie entre estos 8 paises es de: 3994431.62 km2
```

**4. Cantidad de países por continente**

```
=== PAISES POR CONTINENTE ===
Africa: 1 paises
America: 5 paises
Antartida: 0 paises
Asia: 1 paises
Europa: 0 paises
Oceania: 1 paises
```

---

### 7. Salir

```
Saliendo del programa
```
