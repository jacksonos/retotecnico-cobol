import csv
import sys

def procesar_archivo(archivo):
    """
    Procesa el archivo CSV y genera un reporte con el balance final,
    las transacciones de mayor monto (en caso de empate) y el conteo de transacciones.
    """
    try:
        # Inicializar variables
        balance_final = 0.0
        max_monto = float('-inf')
        transacciones_max_monto = []  # Lista para almacenar transacciones con el monto máximo
        conteo_creditos = 0
        conteo_debitos = 0

        # Leer el archivo CSV
        with open(archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Validar que las columnas esperadas existan
            if not {'id', 'tipo', 'monto'}.issubset(reader.fieldnames):
                print("Error: El archivo CSV debe contener las columnas 'id', 'tipo' y 'monto'.")
                sys.exit(1)

            for row in reader:
                try:
                    # Extraer datos de la fila
                    transaccion_id = row['id']
                    tipo = row['tipo']
                    monto = float(row['monto'])

                    # Actualizar balance final
                    if tipo == "Crédito":
                        balance_final += monto
                        conteo_creditos += 1
                    elif tipo == "Débito":
                        balance_final -= monto
                        conteo_debitos += 1
                    else:
                        print(f"Advertencia: Tipo de transacción desconocido '{tipo}' en la fila con ID {transaccion_id}.")
                        continue

                    # Identificar las transacciones de mayor monto
                    if monto > max_monto:
                        max_monto = monto
                        transacciones_max_monto = [(transaccion_id, monto)]  # Reiniciar la lista
                    elif monto == max_monto:
                        transacciones_max_monto.append((transaccion_id, monto))  # Agregar a la lista

                except ValueError:
                    print(f"Advertencia: Valor no numérico en la columna 'monto' para la fila con ID {transaccion_id}.")
                    continue

        # Generar el reporte
        print("\nReporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance_final:.2f}")
        
        # Mostrar todas las transacciones de mayor monto
        if len(transacciones_max_monto) == 1:
            print(f"Transacción de Mayor Monto: ID {transacciones_max_monto[0][0]} - {transacciones_max_monto[0][1]:.2f}")
        else:
            print("Transacciones de Mayor Monto:")
            for transaccion in transacciones_max_monto:
                print(f"  ID {transaccion[0]} - {transaccion[1]:.2f}")
        
        print(f"Conteo de Transacciones: Crédito: {conteo_creditos} Débito: {conteo_debitos}\n")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no fue encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

def main():
    """
    Función principal que maneja la entrada del usuario y llama a la función de procesamiento.
    """
    if len(sys.argv) != 2:
        print("Uso: python app.py <ruta_al_archivo_csv>")
        sys.exit(1)

    archivo = sys.argv[1]
    procesar_archivo(archivo)

if __name__ == "__main__":
    main()