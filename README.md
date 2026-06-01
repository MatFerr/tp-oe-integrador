# **Trabajo Integrador Organizacion Empresarial**
**Introduccion al Proyecto(Esta en el PDF)**
* Consiste en una aplicación que controlará los diferentes caminos lógicos mediante compuertas de decisión que validarán si el empleado tiene saldo suficiente para tomarse las vacaciones o si existen conflictos en los datos ingresados. El bot consultara una base de datos donde están todos los empleados del hotel (todo aquel que posea su legajo) este corroborara alli la información ingresada por el usuario. Asimismo, la robustez del sistema se garantizará a través de una máquina de estados que le otorgará memoria al bot para reconocer exactamente en qué fase de la solicitud se encuentra cada interacción. Finalmente, la simulación contemplará la gestión de excepciones o caminos infelices, programando respuestas alternativas en caso de que el operario introduzca un formato de fecha erróneo o texto en campos numéricos, logrando así una solución integral, resiliente y de alto valor operativo para la organización 

* Es un proyecto sin librerías externas para la manipulación de datos (solo se importan algunas menores. Ej. para el formateo de fechas) esto debido a que se decidió solo utilizar el conocimiento de programación (funciones, métodos, archivos CSV, etc.) vistos en clase. Del mismo modo, se terminó por realizar un simulador en consola. La elección viene de la mano con el punto anterior, evitar el uso de código externo de librerías ni agregarle más complejidad al proyecto. El bot esta codificado con puro conocimiento y metodologías adquiridas en clase 

**La guia del usuario y los diferentes estados de la maquina de estados, se encuentran en el PDF**
**Descripcion del Repositorio**
* *solicitudes.csv**: Archivo '.csv' que contiene las solicitudes de los usuarios almacenadas(Simula una base de datos)
* *archivos.csv**: Archivo '.csv' que almacena todos los trabajadores de la empresa(Simula una base de datos)
* *TpIntegradorOE.py**: Archivo de Python que contiene todo el codigo ejecutable del simulador del ChatBot
* *MarcoTeoricoOE.pdf**: Archivo de tipo PDF donde se encuentra toda la teoria, explicaciones, capturas, guias, etc. Del proyecto en cuestion

**Ejecucion del Programa**
* Descarga del repositorio los archivos CSV y el codigo de Python.
* Abrelo en un IDE de preferencia(Ej: Visual Studio)
* Asegurate de tener un compilador o interprete adecuado que pueda leer e interpretar el codigo de python
* Cambia la direccion de los archivos .csv en la funciones del programa. Escribe la direccion en la que hayas guardado dichos documentos
* Ejecuta el programa
**PAT**
  No se vio la necesidad de añadir un PAT, debido a que no se realizo ninguna consulta a la API de GitHub desde la terminal
