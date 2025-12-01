
from utils.menus import *
from utils.jsonFileHandler import *

GASTOS_FILE = "./database/gastosT.json"

options = (
    "Registrar nuevo gasto",
    "Listar gastos",
    "Calcular total de gastos",
    "Generar reporte de gastos",
    "Salir"
)
while True:
    choice =menu_principal("Simulador de Gastos Personales", options)
    limpiar_pantalla()
    match choice:
        case 1: 
            
            print("="*45)
            print("----------- Registar Nuevo Gasto ------------")
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
            fecha_ingresada = str(input("Ingrese la fecha del gasto (DD/MM/AAAA): "))
            registro= {
                "Monto": monto_ingresado,
                "Categoria": categoria_ingresada,
                "Descripcion": descripcion_ingresada,
                "Fecha": fecha_ingresada   
            }
            dataGastos = readFile(GASTOS_FILE)
            dataGastos.append(registro)
            saveFile(GASTOS_FILE, dataGastos)
      # case 2:    