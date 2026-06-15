# Trabajo Práctico Integrador - Gestión de Datos de Países en Python
Repositorio para el Trabajo Practico Integrador de Programacion 1 - 1er Cuatrimestre 2026

## Integrantes
- Abril Genoveva Ramos Dietmair
- Nicolas Marcelo Chaine

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación en Python que permite gestionar información de diferentes países utilizando estructuras de datos como listas y diccionarios.

El sistema trabaja con un archivo CSV que contiene información de los países, incluyendo:
- Nombre del país.
- Población.
- Superficie en kilómetros cuadrados.
- Continente al que pertenece.

El programa permite realizar distintas operaciones como:
- Agregar un nuevo país.
- Actualizar la población y superficie de un país existente.
- Buscar países por nombre.
- Filtrar países según continente, población o superficie.
- Ordenar los países por diferentes criterios.
- Mostrar estadísticas generales de los datos cargados.

---

## Tecnologías utilizadas

- Python 3.10 o superior. El proyecto fue probado con Python 3.14.2.
- Archivos CSV
- Git y GitHub
- Visual Studio Code

---

## Estructura de datos utilizada

Se utiliza una lista de diccionarios donde cada diccionario representa un país.

Ejemplo:

```python
{
    'nombre': 'Argentina',
    'poblacion': 45376763,
    'superficie': 2780400,
    'continente': 'America'
}
```

---

## Instrucciones de ejecución

1. Descargar o clonar el repositorio desde GitHub.
2. Abrir la carpeta del proyecto en Visual Studio Code o en otra terminal.
3. Verificar que los archivos `aplicacion_tp_integrador_RamosAbril_ChaineNicolas.py` y `paises.csv` se encuentren en la misma carpeta.
4. Abrir una terminal dentro de esa carpeta.
5. Ejecutar el siguiente comando:
6. Utilizar el menú en consola para seleccionar las opciones del sistema.

```bash
python aplicacion_tp_integrador_RamosAbril_ChaineNicolas.py
```
---

## Ejemplos de uso

### Agregar un país

Entrada:
```
Nombre: Chile
Población: 19600000
Superficie: 756102
Continente: America
```

Salida:
```
País agregado correctamente.
```

### Buscar un país

Entrada:
```
Ingrese un país: Argentina
```

Salida:
```
 * Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: America
```

---

## Validaciones implementadas

El sistema controla:
- Campos vacíos.
- Datos numéricos incorrectos.
- Búsquedas sin resultados.
- Errores en la lectura del archivo CSV.
- Filtros inválidos.

---

## Participación de los integrantes

### Abril Genoveva Ramos Dietmair
- Desarrollo del código en Python
- Desarrollo del informe principal
- Diseño y armado del README.md
- Diseño y armado del archivo paises.csv
- Diseño y armado del diagrama de flujo.

### Nicolas Marcelo Chaine
- Desarrollo del código en Python
- Desarrollo del informe principal
- Diseño y armado del README.md
- Armado del repositorio en GitHub
- Pruebas y validaciones.

---

## Enlaces importantes

- [Repositorio GitHub](https://github.com/NicolasChaine/TPI-Programacion1-ChaineNicolas-RamosAbril.git)

- [Video explicativo](https://www.youtube.com/watch?v=2iuJm_hvGmc)

- [Documentación en PDF](./TP_Integrador_Programacion_Informe.pdf)
