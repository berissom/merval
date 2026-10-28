# Merval histórico

Script en Python para descargar la serie histórica diaria del índice Merval desde Yahoo Finance, guardarla en formato CSV y generar un gráfico con sus valores de cierre.

El símbolo utilizado es `^MERV`.

## Requisitos

- Python `3.14` o superior.
- [uv](https://docs.astral.sh/uv/).
- Acceso a Internet para consultar Yahoo Finance.

Las dependencias del proyecto están declaradas en `pyproject.toml` y fijadas en `uv.lock`:

- `yfinance`: descarga los datos financieros.
- `pandas`: procesa y exporta la serie temporal.
- `matplotlib`: genera el gráfico.

## Instalación de uv

Si todavía no tenés `uv` instalado, podés instalarlo con el método recomendado para tu sistema. Por ejemplo, en Linux y macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

En Windows PowerShell:

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

También podés consultar las [instrucciones oficiales de instalación de uv](https://docs.astral.sh/uv/getting-started/installation/).

Verificá la instalación con:

```bash
uv --version
```

## Configuración del proyecto

Cloná el repositorio y entrá en su carpeta:

```bash
git clone <URL_DEL_REPOSITORIO>
cd merval
```

Sincronizá el entorno virtual y las dependencias usando el lockfile:

```bash
uv sync
```

`uv sync` crea el entorno virtual `.venv` si no existe, instala las dependencias y respeta las versiones definidas en `uv.lock`.

## Uso

Ejecutá el script desde la raíz del proyecto:

```bash
uv run main.py
```

No es necesario activar manualmente el entorno virtual: `uv run` utiliza el entorno administrado por el proyecto.

El programa:

1. Descarga toda la información histórica disponible de `^MERV` con frecuencia diaria.
2. Elimina la zona horaria del índice de fechas.
3. Muestra en la terminal las primeras y últimas filas y la cantidad total de registros.
4. Guarda los datos en `merval_historico.csv`.
5. Guarda el gráfico del cierre diario en `merval_historico.png`.
6. Abre el gráfico en una ventana de Matplotlib.

Los archivos de salida se generan en la carpeta desde la que se ejecuta el comando y se sobrescriben en cada ejecución.

## Estructura

```text
.
├── main.py                # Script principal
├── pyproject.toml         # Metadatos y dependencias del proyecto
├── uv.lock                # Versiones bloqueadas por uv
├── .python-version        # Versión de Python del proyecto
├── merval_historico.csv   # Datos descargados (generado)
└── merval_historico.png   # Gráfico generado
```

## Actualizar dependencias

Para agregar una dependencia:

```bash
uv add nombre-del-paquete
```

Para actualizar las dependencias dentro de las restricciones actuales:

```bash
uv lock --upgrade
uv sync
```

## Consideraciones

- Los datos dependen de la disponibilidad y respuesta de Yahoo Finance.
- Si Yahoo Finance no devuelve datos, el programa termina con un error.
- El gráfico requiere un entorno con soporte para abrir ventanas de Matplotlib. En entornos sin interfaz gráfica, se puede conservar el archivo PNG aunque la apertura de la ventana no esté disponible.
- `merval_historico.csv` y `merval_historico.png` son resultados generados; pueden regenerarse ejecutando nuevamente el script.
