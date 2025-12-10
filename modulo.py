"""
Generador de reportes detallados de gastos
Uso: python reporte_detallado.py <fecha_inicio> <fecha_fin> [categoria]
"""

import sys
import os
from datetime import datetime
from json import dumps, load
from utils.menus import validar_fecha
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


GASTOS_FILE = "database/gastos.json"
REPORTS_DIR = "reports/"

def generar_reporte_detallado(fecha_inicio, fecha_fin, categoria=None):
    # Validar fechas
    if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
        print("Error: Formato de fecha inválido. Use DD/MM/AAAA")
        return False
    
    # Leer gastos
    try:
        with open(GASTOS_FILE, 'r') as f:
            gastos = load(f)
    except:
        gastos = []
    
    # Filtrar gastos
    gastos_filtrados = []
    for gasto in gastos:
        if fecha_inicio <= gasto['Fecha'] <= fecha_fin:
            if not categoria or gasto['Categoria'].lower() == categoria.lower():
                gastos_filtrados.append(gasto)
    
    # Calcular totales
    total = sum(g['Monto'] for g in gastos_filtrados)
    
    totales_categoria = {}
    for gasto in gastos_filtrados:
        cat = gasto['Categoria']
        totales_categoria[cat] = totales_categoria.get(cat, 0) + gasto['Monto']
    
    # Crear reporte
    reporte = {
        "rango_fechas": {"inicio": fecha_inicio, "fin": fecha_fin},
        "categoria": categoria or "todas",
        "total_general": round(total, 2),
        "totales_por_categoria": {k: round(v, 2) for k, v in totales_categoria.items()},
        "gastos": [
            {
                "fecha": g['Fecha'],
                "categoria": g['Categoria'],
                "monto": g['Monto'],
                "descripcion": g['Descripcion']
            }
            for g in gastos_filtrados
        ]
    }
    
    # Guardar archivo
    os.makedirs(REPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo = f"{REPORTS_DIR}reporte_detallado_{timestamp}.json"
    
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(dumps(reporte, indent=4, ensure_ascii=False))
    
    # Mostrar resumen
    print(f"\n✓ Reporte generado exitosamente")
    print(f"  Rango: {fecha_inicio} - {fecha_fin}")
    print(f"  Categoría: {categoria or 'Todas'}")
    print(f"  Gastos encontrados: {len(gastos_filtrados)}")
    print(f"  Total: ${total:,.2f}")
    print(f"  Archivo: {archivo}\n")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python reporte_detallado.py <fecha_inicio> <fecha_fin> [categoria]")
        print("Ejemplo: python reporte_detallado.py 01/11/2025 31/12/2025 Comida")
        sys.exit(1)
    
    fecha_inicio = sys.argv[1]
    fecha_fin = sys.argv[2]
    categoria = sys.argv[3] if len(sys.argv) > 3 else None
    
    generar_reporte_detallado(fecha_inicio, fecha_fin, categoria)