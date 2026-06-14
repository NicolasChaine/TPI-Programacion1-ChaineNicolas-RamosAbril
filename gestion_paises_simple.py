import csv

# ------------------------------------------------------------
# Trabajo Práctico Integrador - Programación 1
# Gestión de Datos de Países en Python
#
# Integrantes:
# - Nicolás Chaine
# - Abril Ramos
#
# ------------------------------------------------------------

CONTINENTES_VALIDOS = ["America", "Europa", "Asia", "Africa", "Oceania"]
ARCHIVO_CSV = "paises.csv"


# ------------------------------------------------------------
# FUNCIÓN PARA VALIDAR OPCIONES DE MENÚ
# ------------------------------------------------------------

def elegir_opcion_menu(rango):
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "":
        raise ValueError("La opción no puede estar vacía.")
    elif not opcion.isdigit():
        raise ValueError("La opción ingresada es inválida.")
    elif int(opcion) not in rango:
        raise ValueError("La opción seleccionada está fuera del rango.")

    return int(opcion)


# ------------------------------------------------------------
# FUNCIONES PARA ORDENAMIENTO
# ------------------------------------------------------------

def obtener_nombre(pais):
    return pais["nombre"]


def obtener_poblacion(pais):
    return pais["poblacion"]


def obtener_superficie(pais):
    return pais["superficie"]


# ------------------------------------------------------------
# MANEJO DE CSV
# ------------------------------------------------------------

def cargar_paises_csv():
    paises = []

    try:
        archivo = open(ARCHIVO_CSV, "r", encoding="utf-8", newline="")
        lector = csv.reader(archivo)

        encabezado = next(lector)

        if encabezado != ["nombre", "poblacion", "superficie", "continente"]:
            print("Error: el archivo CSV no tiene las columnas correctas.")
            print("Debe tener: nombre,poblacion,superficie,continente")
            archivo.close()
            return paises

        numero_fila = 2

        for fila in lector:
            if len(fila) != 4:
                print(f"Fila {numero_fila} omitida: cantidad incorrecta de datos.")
            else:
                nombre = fila[0].strip()
                poblacion = fila[1].strip()
                superficie = fila[2].strip()
                continente = fila[3].strip()

                if nombre == "" or poblacion == "" or superficie == "" or continente == "":
                    print(f"Fila {numero_fila} omitida: contiene campos vacíos.")
                elif not poblacion.isdigit():
                    print(f"Fila {numero_fila} omitida: la población debe ser un número.")
                elif not superficie.isdigit():
                    print(f"Fila {numero_fila} omitida: la superficie debe ser un número.")
                elif int(poblacion) <= 0:
                    print(f"Fila {numero_fila} omitida: la población debe ser mayor a cero.")
                elif int(superficie) <= 0:
                    print(f"Fila {numero_fila} omitida: la superficie debe ser mayor a cero.")
                else:
                    pais = {}
                    pais["nombre"] = nombre
                    pais["poblacion"] = int(poblacion)
                    pais["superficie"] = int(superficie)
                    pais["continente"] = continente

                    paises.append(pais)

            numero_fila += 1

        archivo.close()
        print(f"Archivo CSV cargado correctamente. Países cargados: {len(paises)}")

    except FileNotFoundError:
        print(f"No se encontró el archivo {ARCHIVO_CSV}.")
        print("El programa iniciará con la lista de países vacía.")

    except StopIteration:
        print("El archivo CSV está vacío.")

    except Exception as e:
        print(f"Ocurrió un error al leer el archivo CSV: {e}")

    return paises


def guardar_paises_csv(paises):
    try:
        archivo = open(ARCHIVO_CSV, "w", encoding="utf-8", newline="")
        escritor = csv.writer(archivo)

        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

        for pais in paises:
            escritor.writerow([
                pais["nombre"],
                pais["poblacion"],
                pais["superficie"],
                pais["continente"]
            ])

        archivo.close()

    except Exception as e:
        print(f"No se pudieron guardar los cambios en el CSV: {e}")


# ------------------------------------------------------------
# FUNCIONES PRINCIPALES
# ------------------------------------------------------------

def mostrar_paises(paises):
    print("\nLISTADO DE PAÍSES")

    if paises == []:
        print("No hay países cargados.")
    else:
        for pais in paises:
            print(f" * {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")

    input("\nPresione ENTER para volver al menú principal...")


def agregar_pais(paises):
    print("\nAGREGAR PAÍS")

    try:
        nombre = input("Ingrese el nombre del país: ").strip()

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        for pais in paises:
            if nombre.lower() == pais["nombre"].lower():
                raise ValueError("El país ya existe en el sistema.")

        poblacion = input("Ingrese la población: ").strip()

        if poblacion == "":
            raise ValueError("La población no puede estar vacía.")
        elif not poblacion.isdigit():
            raise ValueError("La población debe ser un número entero.")
        elif int(poblacion) <= 0:
            raise ValueError("La población debe ser mayor a cero.")

        superficie = input("Ingrese la superficie en km²: ").strip()

        if superficie == "":
            raise ValueError("La superficie no puede estar vacía.")
        elif not superficie.isdigit():
            raise ValueError("La superficie debe ser un número entero.")
        elif int(superficie) <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")

        continente = input("Ingrese el continente: ").strip()

        if continente == "":
            raise ValueError("El continente no puede estar vacío.")

        nuevo_pais = {}
        nuevo_pais["nombre"] = nombre
        nuevo_pais["poblacion"] = int(poblacion)
        nuevo_pais["superficie"] = int(superficie)
        nuevo_pais["continente"] = continente

        paises.append(nuevo_pais)
        guardar_paises_csv(paises)

        print("País agregado correctamente.")
        print("Los cambios fueron guardados automáticamente en el CSV.")

    except ValueError as e:
        print(f"Error: {e}")

    input("\nPresione ENTER para volver al menú principal...")


def actualizar_pais(paises):
    print("\nACTUALIZAR PAÍS")

    if paises == []:
        print("No hay países cargados.")
        input("\nPresione ENTER para volver al menú principal...")
        return

    try:
        nombre = input("Ingrese el nombre exacto del país a actualizar: ").strip()

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        pais_encontrado = False

        for pais in paises:
            if nombre.lower() == pais["nombre"].lower():
                pais_encontrado = True

                print(f"País encontrado: {pais['nombre']}")
                print(f"Población actual: {pais['poblacion']}")
                print(f"Superficie actual: {pais['superficie']} km²")

                nueva_poblacion = input("Ingrese la nueva población: ").strip()

                if nueva_poblacion == "":
                    raise ValueError("La población no puede estar vacía.")
                elif not nueva_poblacion.isdigit():
                    raise ValueError("La población debe ser un número entero.")
                elif int(nueva_poblacion) <= 0:
                    raise ValueError("La población debe ser mayor a cero.")

                nueva_superficie = input("Ingrese la nueva superficie en km²: ").strip()

                if nueva_superficie == "":
                    raise ValueError("La superficie no puede estar vacía.")
                elif not nueva_superficie.isdigit():
                    raise ValueError("La superficie debe ser un número entero.")
                elif int(nueva_superficie) <= 0:
                    raise ValueError("La superficie debe ser mayor a cero.")

                pais["poblacion"] = int(nueva_poblacion)
                pais["superficie"] = int(nueva_superficie)

                guardar_paises_csv(paises)

                print("País actualizado correctamente.")
                print("Los cambios fueron guardados automáticamente en el CSV.")
                break

        if not pais_encontrado:
            print("No se encontró un país con ese nombre.")

    except ValueError as e:
        print(f"Error: {e}")

    input("\nPresione ENTER para volver al menú principal...")


def buscar_pais(paises):
    print("\nBUSCAR PAÍS")

    if paises == []:
        print("No hay países cargados.")
        input("\nPresione ENTER para volver al menú principal...")
        return

    try:
        busqueda = input("Ingrese el nombre o parte del nombre del país: ").strip()

        if busqueda == "":
            raise ValueError("La búsqueda no puede estar vacía.")

        encontrado = False

        for pais in paises:
            if busqueda.lower() in pais["nombre"].lower():
                print(f" * {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                encontrado = True

        if not encontrado:
            print("No se encontraron países con ese criterio de búsqueda.")

    except ValueError as e:
        print(f"Error: {e}")

    input("\nPresione ENTER para volver al menú principal...")


def filtrar_paises(paises):
    print("\nFILTRAR PAÍSES")

    if paises == []:
        print("No hay países cargados.")
        input("\nPresione ENTER para volver al menú principal...")
        return

    try:
        print("""
Seleccione el tipo de filtro:
1. Filtrar por continente
2. Filtrar por rango de población
3. Filtrar por rango de superficie
4. Volver al menú principal
""")

        opcion_filtro = elegir_opcion_menu([1, 2, 3, 4])

        if opcion_filtro == 1:
            continente = input("Ingrese el continente: ").strip()

            if continente == "":
                raise ValueError("El continente no puede estar vacío.")

            encontrado = False

            for pais in paises:
                if continente.lower() == pais["continente"].lower():
                    print(f" * {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                    encontrado = True

            if not encontrado:
                print("No se encontraron países en ese continente.")

        elif opcion_filtro == 2:
            minimo = input("Ingrese la población mínima: ").strip()
            maximo = input("Ingrese la población máxima: ").strip()

            if minimo == "" or maximo == "":
                raise ValueError("Los valores del rango no pueden estar vacíos.")
            elif not minimo.isdigit() or not maximo.isdigit():
                raise ValueError("Los valores del rango deben ser números enteros.")

            minimo = int(minimo)
            maximo = int(maximo)

            if minimo > maximo:
                raise ValueError("El valor mínimo no puede ser mayor que el valor máximo.")

            encontrado = False

            for pais in paises:
                if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
                    print(f" * {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                    encontrado = True

            if not encontrado:
                print("No se encontraron países en ese rango de población.")

        elif opcion_filtro == 3:
            minimo = input("Ingrese la superficie mínima: ").strip()
            maximo = input("Ingrese la superficie máxima: ").strip()

            if minimo == "" or maximo == "":
                raise ValueError("Los valores del rango no pueden estar vacíos.")
            elif not minimo.isdigit() or not maximo.isdigit():
                raise ValueError("Los valores del rango deben ser números enteros.")

            minimo = int(minimo)
            maximo = int(maximo)

            if minimo > maximo:
                raise ValueError("El valor mínimo no puede ser mayor que el valor máximo.")

            encontrado = False

            for pais in paises:
                if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
                    print(f" * {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                    encontrado = True

            if not encontrado:
                print("No se encontraron países en ese rango de superficie.")

        elif opcion_filtro == 4:
            return

    except ValueError as e:
        print(f"Error: {e}")

    input("\nPresione ENTER para volver al menú principal...")


def ordenar_paises(paises):
    print("\nORDENAR PAÍSES")

    if paises == []:
        print("No hay países cargados.")
        input("\nPresione ENTER para volver al menú principal...")
        return

    try:
        print("""
Seleccione el criterio de ordenamiento:
1. Ordenar por nombre
2. Ordenar por población
3. Ordenar por superficie
""")

        criterio = elegir_opcion_menu([1, 2, 3])

        print("""
Seleccione el tipo de ordenamiento:
1. Ascendente
2. Descendente
""")

        tipo_orden = elegir_opcion_menu([1, 2])

        descendente = False

        if tipo_orden == 2:
            descendente = True

        if criterio == 1:
            paises_ordenados = sorted(paises, key=obtener_nombre, reverse=descendente)
        elif criterio == 2:
            paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=descendente)
        else:
            paises_ordenados = sorted(paises, key=obtener_superficie, reverse=descendente)

        print("\nPAÍSES ORDENADOS")

        for pais in paises_ordenados:
            print(f" * {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")

    except ValueError as e:
        print(f"Error: {e}")

    input("\nPresione ENTER para volver al menú principal...")


def mostrar_estadisticas(paises):
    print("\nESTADÍSTICAS")

    if paises == []:
        print("No hay países cargados.")
        input("\nPresione ENTER para volver al menú principal...")
        return

    pais_mayor_poblacion = paises[0]
    pais_menor_poblacion = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}

    for pais in paises:
        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais

        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        if pais["continente"] in continentes:
            continentes[pais["continente"]] += 1
        else:
            continentes[pais["continente"]] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']} habitantes)")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']} habitantes)")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

    print("\nCantidad de países por continente:")
    for continente in continentes:
        print(f" * {continente}: {continentes[continente]}")

    input("\nPresione ENTER para volver al menú principal...")


# ------------------------------------------------------------
# BLOQUE PRINCIPAL
# ------------------------------------------------------------

paises = cargar_paises_csv()

opcion = 0

print("\nBienvenido al sistema de Gestión de Datos de Países.")

while opcion != 8:
    try:
        print("""
MENÚ PRINCIPAL
1. Mostrar todos los países
2. Agregar un país
3. Actualizar población y superficie de un país
4. Buscar país por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
8. Salir
""")

        opcion = elegir_opcion_menu([1, 2, 3, 4, 5, 6, 7, 8])

        match opcion:
            case 1:
                mostrar_paises(paises)

            case 2:
                agregar_pais(paises)

            case 3:
                actualizar_pais(paises)

            case 4:
                buscar_pais(paises)

            case 5:
                filtrar_paises(paises)

            case 6:
                ordenar_paises(paises)

            case 7:
                mostrar_estadisticas(paises)

            case 8:
                print("Muchas gracias por usar nuestra aplicación.")

    except ValueError as e:
        print(f"Error: {e}")
        input("\nPresione ENTER para continuar...")
