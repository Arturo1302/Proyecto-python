import os
from datetime import datetime   
def menu_principal(title, options):
    choise = 0
    index = 1
    print("="*45)
    print(f"------ {title} -------")
    print("="*45)
    print("" )
    
    for item in options:
        print(f"{index}. {item}")
        index += 1
           
    while True:
        try:
            choise = int(input("\n Seleccione una opción: "))
            if choise not in range (1,len(options)+1):
                print("Opcion no valida...")
            else: break
        except ValueError:
            print("Su eleccion debe ser un numero...")
    return choise

def limpiar_pantalla(): 
    input("Presione Enter para continuar...")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def listar_gastos(title, options2):
    choise = 0
    index = 1
    print("="*45)
    print(f"-----------  {title} ------------")
    print("="*45)
    print("")
    for item in options2:
        print(f"{index}. {item}")
        index += 1
           
    while True:
        try:
            choise = int(input("\n Seleccione una opción: "))
            if choise not in range (1,len(options2)+1):
                print("Opcion no valida...")
            else: break
        except ValueError:
            print("Su eleccion debe ser un numero...")
    return choise

def calcular_total_gastos(title, options3):
    choise = 0
    index = 1
    print("="*45)
    print(f"-----------  {title} ------------")
    print("="*45)
    print("")
    for item in options3:
        print(f"{index}. {item}")
        index += 1
           
    while True:
        try:
            choise = int(input("\n Seleccione una opción: "))
            if choise not in range (1,len(options3)+1):
                print("Opcion no valida...")
            else: break
        except ValueError:
            print("Su eleccion debe ser un numero...")
    return choise
def generar_reporte(title, options4):
    choise = 0
    index = 1
    print("="*45)
    print(f"-----------  {title} ------------")
    print("="*45)
    print("")
    for item in options4:
        print(f"{index}. {item}")
        index += 1
           
    while True:
        try:
            choise = int(input("\n Seleccione una opción: "))
            if choise not in range (1,len(options4)+1):
                print("Opcion no valida...")
            else: break
        except ValueError:
            print("Su eleccion debe ser un numero...")
    return choise

def validar_fecha(fecha_str):
    """Valida y convierte una fecha en formato DD/MM/AAAA"""
    try:
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        return None

def validar_mes_ano(mes_ano_str):
    try:
        return datetime.strptime(mes_ano_str, "%m/%Y")
    except ValueError:
        return None