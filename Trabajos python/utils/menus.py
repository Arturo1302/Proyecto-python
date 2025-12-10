import os
from datetime import datetime   
def menu(title, options):
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
    
    # Esta funcion es para no superar el gasto maximo diario por fecha 
def gasto_maximodiario(monto_ingresado,gasto_dia, gasto_maximo):
    while True:
        gasto_maximo == 200000
        porcentaje_gasto = (gasto_dia + monto_ingresado) / gasto_maximo * 100
        if (gasto_dia + monto_ingresado) > gasto_maximo:
            print("Alerta: Has superado el gasto maximo diario de $200,000")
            return False
        else:
            print("Gasto dentro del limite diario. Lleva gastado el {:.2f}% del limite.".format(porcentaje_gasto))
            return True
    
# Esta funcion es para no superar el gasto maximo semanal y se acumule segun la fecha
def gasto_maximosemanal(monto_ingresado,gasto_semana, gasto_maximo):
    while True:
        gasto_maximo == 1200000
        porcentaje_gasto = (gasto_semana + monto_ingresado) / gasto_maximo * 100
        if (gasto_semana + monto_ingresado) > gasto_maximo:
            print("Alerta: Ha superado el gasto maximo semanal de $1,200,000")
            return False
        else:
            print("Gasto dentro del limite semanal. Lleva gastado el {:.2f}% del limite.".format(porcentaje_gasto))
            
            return True
 
 # Esta funcion es para no superar el gasto maximo por categoria
def gasto_maximocategoria(monto_ingresado,gasto_categoria, gasto_maximo):
    while True:
        gasto_maximo == 500000
        porcentaje_gasto = (gasto_categoria + monto_ingresado) / gasto_maximo * 100
        if (gasto_categoria + monto_ingresado) > gasto_maximo:
            print("Alerta: Ha superado el gasto maximo por categoria de $500,000")
            return False
        else:
            print("Gasto dentro del limite por categoria. Lleva gastado el {:.2f}% del limite.".format(porcentaje_gasto))
            return True  