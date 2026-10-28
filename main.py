import yfinance as yf
import matplotlib.pyplot as plt

# Símbolo del índice Merval en Yahoo Finance
ticker = "^MERV"

# Descargar toda la serie histórica disponible, con frecuencia diaria
merval = yf.Ticker(ticker).history(
    period="max",
    interval="1d",
    auto_adjust=False,
)

if merval.empty:
    raise RuntimeError("Yahoo Finance no devolvió datos.")

# Eliminar información de zona horaria del índice temporal
merval.index = merval.index.tz_localize(None)

# Guardar la serie completa en CSV
merval.to_csv("merval_historico.csv", index_label="Fecha")

print(merval.head())
print(merval.tail())
print(f"\nCantidad de registros: {len(merval)}")
print("Archivo guardado: merval_historico.csv")

# Graficar el cierre diario
merval["Close"].plot(
    figsize=(12, 5),
    title="Índice Merval (^MERV)",
    xlabel="Fecha",
    ylabel="Puntos del índice",
    grid=True,
)

plt.tight_layout()
plt.savefig("merval_historico.png", dpi=150)
plt.show()
