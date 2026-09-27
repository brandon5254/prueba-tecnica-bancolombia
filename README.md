# Prueba Técnica - Analista de Evolución

Proyecto desarrollado en Python para procesar información de ventas desde un archivo Excel y generar un resumen por vendedor y por mes.

## Autor

Brandon Eduardo Tobar Sánchez

## Descripción

El programa toma el archivo `datos_ventas.xlsx`, realiza las transformaciones solicitadas y genera un nuevo archivo llamado `resumen_ventas.xlsx`.

El proceso realiza lo siguiente:

- carga el archivo Excel;
- completa los valores faltantes de `Total_Venta`;
- convierte la columna `Fecha` a formato fecha;
- filtra las ventas del año 2023;
- crea la columna `Mes`;
- calcula el total de ventas por vendedor;
- calcula el total de ventas por mes;
- genera el archivo final en Excel.

## Estructura general

```text
datos_ventas.xlsx
        |
        v
     EXTRACT
        |
        v
    TRANSFORM
        |
        v
   AGGREGATE
        |
        v
      LOAD
        |
        v
resumen_ventas.xlsx

Instalación
1. Clonar el repositorio
git clone https://github.com/brandon5254/prueba-tecnica-bancolombia.git

2. Entrar a la carpeta del proyecto
cd prueba-tecnica-bancolombia

3. Crear el entorno virtual
python -m venv .venv

4. Activar el entorno virtual
En PowerShell:
.\.venv\Scripts\Activate.ps1

En CMD:
.venv\Scripts\activate

5. Instalar las dependencias
pip install -r requirements.txt

Ejecución
Para ejecutar el proceso:
python main.py

Al finalizar se mostrará un mensaje similar a:
Iniciando proceso ETL...
Proceso finalizado correctamente.
Archivo generado: data/gold/resumen_ventas.xlsx

Archivo generado
El resultado se guarda en:
data/gold/resumen_ventas.xlsx

El archivo contiene dos hojas:
- Resumen_Ventas
- Ventas_Mensuales
Pruebas
Para ejecutar las pruebas:
python -m pytest -v

Resultado esperado:
4 passed

Tecnologías utilizadas
- Python
- Pandas
- OpenPyXL
- PyYAML
- Pytest