# Prueba Técnica - Analista de Evolución

Proyecto desarrollado en Python para procesar información de ventas desde un archivo Excel y generar un resumen por vendedor y por mes.

## Autor

**Brandon Eduardo Tobar Sánchez**

## Descripción

El programa toma el archivo `datos_ventas.xlsx`, procesa la información solicitada y genera un nuevo archivo llamado `resumen_ventas.xlsx`.

El proceso realiza lo siguiente:

- Carga los datos desde Excel usando Pandas.
- Completa los valores faltantes de `Total_Venta`.
- Convierte la columna `Fecha` a formato datetime.
- Filtra las ventas del año 2023.
- Crea la columna `Mes`.
- Calcula el total de ventas por vendedor.
- Calcula el total de ventas por mes.
- Genera el archivo final en Excel.

## Flujo del proceso

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
```

## Requisitos

- Python 3.11 o superior.
- Git.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/brandon5254/prueba-tecnica-bancolombia.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd prueba-tecnica-bancolombia
```

### 3. Crear el entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En CMD:

```cmd
.venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

Desde la raíz del proyecto, ejecutar:

```bash
python main.py
```

Al finalizar se mostrará un mensaje similar a:

```text
Iniciando proceso ETL...
Proceso finalizado correctamente.
Archivo generado: data/gold/resumen_ventas.xlsx
```

## Archivo generado

El resultado se guarda en:

```text
data/gold/resumen_ventas.xlsx
```

El archivo contiene dos hojas:

- `Resumen_Ventas`: total de ventas por vendedor.
- `Ventas_Mensuales`: total de ventas por mes.

## Pruebas

Para ejecutar las pruebas:

```bash
python -m pytest -v
```

Las pruebas validan la extracción, transformación, agrupación de datos y generación del archivo Excel.

## Tecnologías utilizadas

- Python
- Pandas
- OpenPyXL
- PyYAML
- Pytest