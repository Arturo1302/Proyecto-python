
from utils.menus import *
from utils.jsonFileHandler import *
from tabulate import tabulate
GASTOS_FILE = "gastos.json"

options = (
    "Registrar nuevo gasto",
    "Listar gastos",
    "Calcular total de gastos",
    "Generar reporte de gastos",
    "Salir"
)

options2 = (
    "Ver todos los gastos",
    "Filtrar gastos por categoria",
    "Filtrar gastos por rango de fechas",
    "Volver al menu principal"
)

options3 = (
    "Calcular total diario",
    "Calcular total semanal",
    "Calcular total mensual",
    "Regresar al menu principal"
)
options4 = (
    "Reporte diario",
    "Reporte semanal",
    "Reporte mensual",
    "Volver al menu principal"
)
while True:
    choice =menu_principal("Simulador de Gastos Personales", options)
    limpiar_pantalla()
    match choice:
        case 1: 
            
            print("="*45)
            print("----------- Registrar Nuevo Gasto ------------")
            print("="*45)
            while True:
                try:    
                    monto_ingresado = float(input("Ingrese el monto del gasto: $"))
                    if monto_ingresado <= 0:
                        print("Error: El monto debe ser mayor a 0")
                        continue
                    break
                except ValueError:
                        print("Error: Debe ingresar un número válido")

            categoria_valida = ["Comida", "Transporte", "Gastos personales", "Salud", "Otros"]
            while True:
                 
                categoria_ingresada = input("Ingrese la categoria del gasto: (Comida, Transporte, Gastos personales, Salud, Otros) ")
                categoria_encontrada = None
                for categoria in categoria_valida:
                    if categoria_ingresada.lower() == categoria.lower():
                        categoria_encontrada = categoria
                        break
                if categoria_encontrada:
                    categoria_ingresada = categoria_encontrada
                    break
                else :
                        print("Categoria no valida. Intente de nuevo.")
                    
            
            descripcion_ingresada = str(input("Ingrese una descripcion del gasto:  "))   


            while True:
                fecha_ingresada = input("Ingrese la fecha del gasto (DD/MM/AAAA): ")
                if validar_fecha(fecha_ingresada):
                    break
                else:
                    print("Error: Formato de fecha invalido. Use DD/MM/AAAA")  
                
            registro= {
                "Monto": monto_ingresado,
                "Categoria": categoria_ingresada,
                "Descripcion": descripcion_ingresada,
                "Fecha": fecha_ingresada   
            }
            dataGastos = readFile(GASTOS_FILE)
            dataGastos.append(registro)
            saveFile(GASTOS_FILE, dataGastos)
            limpiar_pantalla()    
        case 2:    
            while True:
                choice=(listar_gastos("Listado de Gastos", options2))
                limpiar_pantalla()
                match choice:
                    case 1:
                        print("="*45)
                        print("----------- Todos los Gastos ------------")
                        print("="*45)
                        dataGastos = readFile(GASTOS_FILE)
                        if not dataGastos:
                            print("No hay gastos registrados.")
                        else:
                            tabla_datos =[]
                            for gasto in dataGastos:
                                tabla_datos.append([gasto['Monto'], gasto['Categoria'], gasto['Descripcion'], gasto['Fecha']])
                            print(tabulate(tabla_datos, headers=["Monto", "Categoria", "Descripcion", "Fecha"], tablefmt="fancy_grid"))
                            input("Presione Enter para volver al menu...")  
                            limpiar_pantalla()
                    case 2:
                        print("="*45)
                        print("------- Filtrar Gastos por Categoria -------")
                        print("="*45)
                        categoria_filtro = input("Ingrese cual categoria (Comida, Transporte, Gastos personales, Salud, Otros): ")
                        dataGastos = readFile(GASTOS_FILE)
                        gastos_filtrados = [gasto for gasto in dataGastos if gasto['Categoria'].lower() == categoria_filtro.lower()]

                        if not gastos_filtrados:
                            print(f"No hay gastos registrados en la categoria '{categoria_filtro}'.")
                        else:
                            tabla_datos =[]
                            for gasto in gastos_filtrados:
                                tabla_datos.append([gasto['Monto'], gasto['Categoria'], gasto['Descripcion'], gasto['Fecha']])
                            print(tabulate(tabla_datos, headers=["Monto", "Categoria", "Descripcion", "Fecha"], tablefmt="fancy_grid"))
                            input("Presione Enter para volver al menu...")  
                            limpiar_pantalla()


                            
                    case 3:
                        print("="*45)
                        print("----- Filtrar Gastos por Rango de Fechas -----")
                        print("="*45)
                        fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/AAAA): ")
                        fecha_fin = input("Ingrese la fecha de fin (DD/MM/AAAA): ")
                        if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
                            print("Error: Formato de fecha invalido. Use DD/MM/AAAA")
                        else:
                            dataGastos = readFile(GASTOS_FILE)
                            gastos_filtrados = []
                            for gasto in dataGastos:
                                if fecha_inicio <= gasto['Fecha'] <= fecha_fin:
                                    gastos_filtrados.append(gasto)
                            if not gastos_filtrados:
                                print(f"No hay gastos registrados entre {fecha_inicio} y {fecha_fin}.")
                            else:
                                tabla_datos =[]
                                for gasto in gastos_filtrados:
                                    tabla_datos.append([gasto['Monto'], gasto['Categoria'], gasto['Descripcion'], gasto['Fecha']])
                                print(tabulate(tabla_datos, headers=["Monto", "Categoria", "Descripcion", "Fecha"], tablefmt="fancy_grid"))
                                input("Presione Enter para volver al menu...")  
                                limpiar_pantalla()
                    case 4:
                        break
        case 3:
            while True:
                choice = calcular_total_gastos("Calcular Total de Gastos", options3)
                limpiar_pantalla()
                match choice:
                    case 1:
                        print("="*45)
                        print("--------- Calcular Total Diario ---------")
                        print("="*45)
                        dataGastos = readFile(GASTOS_FILE)
                        
                    case 2:
                        print("="*45)
                        print("-------- Calcular Total Semanal --------")
                        print("="*45)
                    case 3:
                        print("="*45)
                        print("-------- Calcular Total Mensual --------")
                        print("="*45)   
                    case 4:
                        break    
        case 4:
            while True:               
                choice = generar_reporte("Generar Reporte de Gastos", options4)
                limpiar_pantalla()
                match choice:
                    case 1:     
                        print("="*45)
                        print("----------- Reporte Diario ------------")
                        print("="*45)
                        fecha = input("Ingrese la fecha para el reporte (DD/MM/AAAA): ")
                        if not validar_fecha(fecha):
                            print("Error: Formato de fecha invalido. Use DD/MM/AAAA")
                        else:
                            gastos_dia = []
                            dataGastos = readFile(GASTOS_FILE)
                            for gasto in dataGastos:
                                if gasto['Fecha'] == fecha:
                                    gastos_dia.append(gasto)
                            if not gastos_dia:
                                print(f"No hay gastos registrados en la fecha {fecha}.")
                            else:
                                tabla_datos =[]
                                for gasto in gastos_dia:
                                    tabla_datos.append([gasto['Monto'], gasto['Categoria'], gasto['Descripcion'], gasto['Fecha']])
                                print(tabulate(tabla_datos, headers=["Monto", "Categoria", "Descripcion", "Fecha"], tablefmt="fancy_grid"))
                                input("Presione Enter para volver al menu...")  
                                limpiar_pantalla()
                        readFile(GASTOS_FILE)
                        
                    case 2:
                        print("="*45)
                        print("---------- Reporte Semanal -----------")    
                        print("="*45)
                        fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/AAAA): ")
                        fecha_fin = input("Ingrese la fecha de fin (DD/MM/AAAA): ")
                        if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
                            print("Error: Formato de fecha invalido. Use DD/MM/AAAA")
                        else:
                            gastos_semana = []
                            dataGastos = readFile(GASTOS_FILE)
                            for gasto in dataGastos:
                                if fecha_inicio <= gasto['Fecha'] <= fecha_fin:
                                    gastos_semana.append(gasto)
                            if not gastos_semana:
                                print(f"No hay gastos registrados entre {fecha_inicio} y {fecha_fin}.")
                            else:
                                tabla_datos =[]
                                for gasto in gastos_semana:
                                    tabla_datos.append([gasto['Monto'], gasto['Categoria'], gasto['Descripcion'], gasto['Fecha']])
                                print(tabulate(tabla_datos, headers=["Monto", "Categoria", "Descripcion", "Fecha"], tablefmt="fancy_grid"))
                                input("Presione Enter para volver al menu...")  
                                limpiar_pantalla()
                    case 3:
                        print("="*45)
                        print("---------- Reporte Mensual -----------")
                        print("="*45)   
                    case 4:
                        break    
        case 5:
            print("Gracias por usar el simulador de gastos personales. ¡Hasta luego!")
            break
 