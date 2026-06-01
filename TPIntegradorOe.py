import csv
from datetime import datetime, timedelta
import locale


#Maquina de estados del programa
estados = ["estado_inicial", "esperando_opcion", "esperando_datos", "esperando_validacion", "muestra_dias", "validacion_solicitud", "esperando_dias", "esperando_fecha", "esperando_confirmacion"]
#Variable que almacenara el estado en el que el usuario se encuentra en el programa
estado_actual = estados[0]
#Mientras salir sea False, el ChatBot se seguira ejecutando
salir = False
#Guarda el usuario traido de la base de datos
usuario = []
#Guarda la solicitud que el sistema trae de la base de datos. Posteriormente almacena la nueva solicitud
solicitud = []

#Guarda los datos que el usuario ingresa en el 'tercer estado', luego se válidan
usuarioIngresado = {
   "area" : "",
   "legajo": "",
}

#Guarda la opcion que el usuario elige en el menu principal
opcionUsuario = 0

#Configuracion de la libreria de fechas
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 

#FUNCIONES DEL CHATBOT

#Funcion 1: Conecta con el archivo CSV y trae el usuario que coincida con los datos enviados como argumento
def traerUsuario(legajo, area):
 usuario = []
 with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegradorOE\empleados.csv', mode='r', newline="", encoding='utf-8') as fichero:
    lector = csv.reader(fichero)
    for fila in lector:
        if(fila[0] == legajo and fila[1] == area):
           usuario = fila
    return usuario

#Funcion 2: Conecta con la base de datos y trae todas las solicitudes que coincidan con el legajo del usuario ingresado como argumento
def traerSolicitudes(legajo):
 global solicitud
 solicitud = []
 with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegradorOE\solicitudes.csv', mode='r', newline='', encoding='utf-8') as fichero:
    lector = csv.reader(fichero)
    for fila in lector:
        if(not fila): continue
        if(fila[0] == legajo):
           solicitud = fila
    return solicitud
 
#Funcion 3: Guarda la solicitud creada por el usuario en el archivo CSV 
def guardarSolicitud(array):
    with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegradorOE\solicitudes.csv', newline='', mode='a', encoding='utf-8') as fichero:
      lector = csv.writer(fichero)
      lector.writerow(array)

#Funcion 4: Actualiza la cantidad de dias disponibles del usuario, en el archivo CSV
def actualizarUsuario(legajo, diasUsados):
   filasActualizadas = []
   with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegradorOE\empleados.csv', mode='r', newline='', encoding='utf-8') as fichero:
    lector = csv.reader(fichero)
    cabecera = next(lector)
    filasActualizadas.append(cabecera)
    for fila in lector:
       if fila[0] == legajo:
          numeroAnterior = int(fila[3])
          fila[3] = numeroAnterior - int(diasUsados)
       filasActualizadas.append(fila)
   with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegradorOE\empleados.csv', mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(filasActualizadas)

# Bucle principal el cual se ejecuta constantemente hasta que el usuario decida salir
while(salir == False):
        
        # Primer Estado: Mensaje de Bienvenida
        if(estado_actual == estados[0]):
         print("Hola! Soy Nemo, tu asistente virtual para gestionar tus vacaciones...")
         estado_actual = estados[1]

         # Segundo Estado: Menu Principal
        elif(estado_actual == estados[1]):
           print("1) Ver dias disponibles")
           print("2) Solicitar vacaciones")
           print("3) Salir")
           opcion = input("Que deseas hacer hoy?: ")
           if(opcion == "1" or ("dias" in opcion.lower() and not "novacaciones" in opcion.lower())):
              opcionUsuario = 1
              estado_actual = estados[2]
           elif(opcion == "2" or "vacaciones" in opcion.lower()):
              opcionUsuario = 2
              estado_actual = estados[2]
           elif(opcion == "3" or opcion.lower() == "salir"):
              print("Hasta la próxima! :)")
              salir = True
           else:
              print("Ups! No conozco esa instruccion. Vayamos de nuevo!")

         # Tercer Estado: Legajo y Area del trabajador
        elif(estado_actual == estados[2]):
           user_legajo = ""
           user_area = ""
           user_legajo = input("Dame tu legajo de trabajador: ")

           if( not user_legajo.isdigit()):
              print("Por favor, ingresa un legajo númerico válido!")
           else:
              usuarioIngresado["legajo"] = user_legajo
              user_area = input("En que area trabajas: ")
              if( not user_area.isalpha() or user_area == ""):
                 print("Por favor, ingresa un area laboral válida!")
              else:
                 usuarioIngresado["area"] = user_area
                 estado_actual = estados[3]

         # Cuarta Estado: Busqueda del trabajador en la BD
        elif(estado_actual == estados[3]):
           usuario = traerUsuario(usuarioIngresado["legajo"], usuarioIngresado["area"])
           if(len(usuario) == 0):
              
              #Mientras se introduzca una opcion que no sea ni 'si' ni 'no', el bucle se sigue ejecutando
              opcion = ""
              while(opcion.lower() != "si" and opcion.lower() != "no"):
                opcion = input("Ups! Ocurrio un error, legajo o area no válida. Desea intentar de nuevo? (si/no): ")
                if(opcion.lower() == "si"):
                    estado_actual = estados[2]
                elif(opcion.lower() == "no"):
                    estado_actual = estados[1]
                else:
                   print("Opcion no válida!")
           else:
                if(opcionUsuario == 1):
                   estado_actual = estados[4]
                else:
                   estado_actual = estados[5] 

         # Quinto Estado: Muestra Dias Disponibles
        elif(estado_actual == estados[4]):
           dias_disponibles = int(usuario[3])

           if(int(dias_disponibles) == 0):
              print("Vaya! Parece que no tienes dias libres disponibles")
           else:
              print(f"Tienes un total de {dias_disponibles} dias disponibles aún! ")

              #El loop sigue ejecutandose hasta que la respuesta sea la solicitada
              opcion = ""
              while(opcion.lower() != "si" and opcion.lower() != "no"):
                opcion = input("Deseas solicitar vacaciones? (si/no): ") 
                if(opcion.lower() == "si"):
                    estado_actual = estados[3]
                    opcionUsuario = 2
                elif(opcion.lower() == "no"):
                    estado_actual = estados[0]
                else:
                   print("Opcion no válida!")

         # Sexto Estado: Carga de solicitudes previas del usuario
        elif(estado_actual == estados[5]):
         solicitud = traerSolicitudes(usuario[0])
         if(len(solicitud) == 0):
           estado_actual = estados[6]
         else:
           if(solicitud[3] == "activo"):
                 print("Ya tienes una solicitud activa...")
                 print(f"Legajo: {solicitud[0]} | Fecha Inicio: {solicitud[2].split("=")[0]} | Fecha Fin: {solicitud[2].split("=")[1]}")
                 estado_actual = estados[6]
           elif(solicitud[3] == "pendiente"):
              print(f"Ya tienes una solicitud de vacaciones en 'pendiente'!")

              #El while se ejecuta infinitamente hasta que no se ingrese la respuesta esperada
              opcion = ""
              while(opcion.lower() != "si" and opcion.lower() != "no"):
                opcion = input("Deseas ver cuantos dias libres te quedan? (si/no): ") 
                if(opcion.lower() == "si"):
                    estado_actual = estados[3]
                    opcionUsuario = 1
                elif(opcion.lower() == "no"):
                    estado_actual = estados[0]
                else:
                   print("Opcion no válida!")
           
         # Septimo Estado: Dias de vacaciones solicitados
        elif(estado_actual == estados[6]):
            diasSolicitados = input("Cuantos dias quieres solicitar: ")

            #Validaciones de la variable diasSolicitados, debe ser un alfanumerico, mayor a 0 y debe ser menor a la cantidad de dias disponibles registrados en la BD
            if(not diasSolicitados.isdigit() or int(diasSolicitados) <= 0):
               print("Por favor ingresa un numero válido de dias")
            else:
               if(int(usuario[3]) <= 0):
                  print("Vaya! Parece que no tienes dias disponibles!")
                  estado_actual = estados[1]
               elif(int(usuario[3]) < int(diasSolicitados)):
                print(f"Ups! Parece que no tienes suficientes dias libres. Tus dias libres: {usuario[3]}")
               else:
                     solicitud = []
                     solicitud.append(usuarioIngresado["legajo"])
                     solicitud.append(diasSolicitados)
                     estado_actual = estados[7]

         # Octavo Estado: Fechas de la vacaciones
        elif(estado_actual == estados[7]):
           fecha_hoy = datetime.now().date()
           try:
              fechaIngresadaInicio = input("Ingresa la fecha de inicio de las vacaciones(AAAA-MM-DD): ")
              fecha_validadaInicio = datetime.strptime(fechaIngresadaInicio, "%Y-%m-%d").date()
           except ValueError:
              print("Ups! Formato de fecha inválido. Recordá usar el formato AAAA-MM-DD.")
              continue
           else:
                 diasSolicitados = int(solicitud[1]) - 1
                 fechaFinal = timedelta(days=diasSolicitados)
                 fecha_validadaFinal = fecha_validadaInicio + fechaFinal
                 if(fecha_hoy > fecha_validadaFinal or fecha_hoy > fecha_validadaInicio):
                    print("Ups! Parece que ingresaste una fecha ya ocurrio!")
                    continue
                 diferencia = fecha_validadaFinal - fecha_validadaInicio
                 diasFecha = diferencia.days

                 #Formateo de fechas con funcion brindada por ChatGpt(Visto en el PDF)
                 fecha_objeto_inicio = datetime.strptime(solicitud[2].split("=")[0], "%Y-%m-%d")
                 fecha_objeto_final = datetime.strptime(solicitud[2].split("=")[1], "%Y-%m-%d")
                 fecha_amigable_inicio = fecha_objeto_inicio.strftime("%A, %d de %B de %Y")
                 fecha_amigable_final = fecha_objeto_final.strftime("%A, %d de %B de %Y")

                 if(diasFecha != diasSolicitados):
                    print("Ups! Los dias solicitados no coinciden con la cantidad de dias ingresados en las fechas anteriores")
                    continue
                 else:
                    solicitud.append("=".join([fechaIngresadaInicio, str(fecha_validadaFinal)]))
                    estado_actual = estados[8]
         
         #Noveno Estado: Resumen de la Solicitud
        elif(estado_actual == estados[8]):
            print("\n" + "="*40)
            print("==SOLICITUD DE VACACIONES==")
            print("="*40)
            print(f"Empleado: {usuario[2]}")
            print(f"Legajo: {usuario[0]}")
            print(f"Dias Solicitados: {solicitud[1]}")
            print(f"Fecha Inicio: {fecha_amigable_inicio}")
            print(f"Fecha Final: {fecha_amigable_final}")
            print("="*40)

            opcion = ""

            #Solo se termina si se escribe 'si' o 'no', sigue su ejecucion en una respuesta distinta
            while(not opcion.lower() in ["si", "sí"] and opcion.lower() != "no"):
                opcion = input("Deseas enviar la solicitud de vacaciones?(si/no): ") 
                if(opcion.lower() in ["si", "sí"]):
                    solicitud.append("pendiente")
                    guardarSolicitud(solicitud)
                    actualizarUsuario(solicitud[0], solicitud[1])
                    print("Solicitud enviada a RRHH correctamente!")
                elif(opcion.lower() == "no"):
                    print("No se ha enviado la solicitud")
                else:
                   print("Opcion no válida!")
            estado_actual = estados[0]
              
