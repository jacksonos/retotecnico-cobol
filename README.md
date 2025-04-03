# 📊 Procesador de Transacciones CSV

## 🚀 Introducción
Este proyecto es una aplicación de línea de comandos (CLI) en Python que procesa archivos CSV con transacciones bancarias. Su propósito es generar un reporte detallado basado en las transacciones contenidas en el archivo.

## 🎯 Objetivo
El objetivo de esta aplicación es procesar un archivo CSV con transacciones bancarias y generar un reporte que incluya:

- 📈 **Balance Final**: Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".
- 💰 **Transacción de Mayor Monto**: Identificar el ID y el monto de la transacción con el valor más alto.
- 🔢 **Conteo de Transacciones**: Número total de transacciones para cada tipo ("Crédito" y "Débito").

## 🛠️ Instrucciones de Ejecución
### 📌 Requisitos previos
- 🐍 Python 3.x instalado en tu sistema.

### ▶️ Ejecución del programa
1. 📥 Clona este repositorio o descarga los archivos.
2. 📂 Ubica un archivo CSV con las columnas `id`, `tipo` y `monto` en la misma carpeta del script.
3. 🖥️ Abre una terminal y navega hasta la carpeta del proyecto.
4. ⌨️ Ejecuta el siguiente comando:
   ```sh
   python app.py <ruta_al_archivo_csv>
   ```
   Ejemplo:
   ```sh
   python app.py ejemplo.csv
   ```

## 🔍 Enfoque y Solución
El programa sigue los siguientes pasos:
1. 📑 Lee el archivo CSV verificando que contenga las columnas requeridas.
2. ⚙️ Procesa cada fila para:
   - ➕ Sumar los montos de crédito al balance final.
   - ➖ Restar los montos de débito al balance final.
   - 🔄 Contar la cantidad de transacciones de cada tipo.
   - 🔝 Identificar las transacciones con el monto más alto.
3. 📊 Imprime un reporte con el balance final, las transacciones más altas y el conteo de créditos y débitos.

## 📁 Estructura del Proyecto
```
/
|-- 📝 app.py               # Script principal del proyecto
|-- 📄 transacciones.csv    # Archivo de ejemplo para pruebas
|-- 📜 README.md            # Documentación del proyecto
```

