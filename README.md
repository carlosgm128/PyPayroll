
# ACME PyPayroll

Presentamos ACME PyPayroll: su herramienta de procesamiento de pagos eficiente basada en horas trabajadas

La gestión de la nómina puede ser una tarea que requiere mucho tiempo, especialmente cuando se trata de calcular los pagos en función de las horas trabajadas. Es por eso que estamos orgullosos de presentar ACME PyPayroll, una poderosa herramienta diseñada para agilizar y automatizar el proceso de cálculo de pagos por horas trabajadas.

PyPayroll ofrece una solución perfecta tanto para empresas como para individuos, eliminando la necesidad de cálculos manuales. Con su fácilidad de usar y su sólida funcionalidad, PyPayroll facilita la generación de informes de pago precisos y oportunos, lo que garantiza una compensación justa para todos.

# Arquitectura

## Estructura de capas
__1: Domain__: La capa de dominio representa las entidades de la aplicación. Debe ser independiente de cualquier marco o tecnología específica. En su caso, la carpeta Modelos puede considerarse parte de la capa de dominio. Contiene las clases Usuario, Día, que representan las entidades y conceptos centrales de la applicacion

__2: Aplicación__: la capa de aplicación contiene los casos de uso y la lógica específica de la aplicación que organiza las entidades y los servicios del dominio. Actúa como un puente entre el dominio y las capas de infraestructura. En este caso, Pago y Utilidades pueden considerarse parte de la capa de aplicación.

__3: Capa de infraestructura__: la capa de infraestructura se ocupa de las dependencias externas, como bases de datos, manejo de archivos externos, API. Incluye detalles de implementación y código específico de la infraestructura. En su caso, la carpeta Config puede considerarse parte de la capa de infraestructura pues esta alberga data de los turnos configurados los cuales pueden estar en una base de datos.



# ¿Cómo funciona PyPayroll?
Comienza importando un archivo de texto que contiene datos de cronometraje, donde cada entrada esta representada el nombre y las horas trabajadas de un empleado. Una vez que se importan los datos, PyPayroll utiliza algoritmos para calcular el total de horas, teniendo en cuenta las horas trabajadas en diferentes turnos de la jornada. Luego calcula las ganancias correspondientes para cada empleado, generando resúmenes de pago completos.

¡Pruebe PyPayroll hoy y experimente el poder del procesamiento de pagos optimizado! Simplifique sus tareas de nómina, ahorre tiempo y garantice una compensación justa para sus empleados trabajadores".

# ¿Como usar ACME PyPayroll?

Metodo 1:

1: Abre la consola o terminal en tu sistema operativo.

2: Navega hasta la ubicación donde tienes guardado el archivo PyPayroll.

3: Ejecuta el siguiente comando:
```bash
    python pypayroll.py --path=<ruta_del_archivo.txt>
```
Asegúrate de reemplazar *<ruta_del_archivo.txt>* con la ruta completa del archivo de texto que contiene las horas trabajadas.

PyPayroll procesará automáticamente el archivo y generará los informes de pago correspondientes.

Metodo 2:

1: Abre la consola o terminal en tu sistema operativo.

2: Navega hasta la ubicación donde tienes guardado el archivo PyPayroll.

3: Ejecuta el siguiente comando:

```shell
    python pypayroll.py
```

4: A continuación, se te solicitará ingresar la ruta del archivo de texto que contiene las horas trabajadas. Ingresa la ruta y presiona Enter.

4.1:(OPCIONAL) Repite el paso 4 dos veces más, ingresando las rutas completas de los archivos adicionales si es necesario.

6: PyPayroll procesará los archivos proporcionados y generará los informes de pago correspondientes.