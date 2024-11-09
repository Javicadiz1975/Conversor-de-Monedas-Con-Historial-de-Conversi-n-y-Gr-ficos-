import requests
import pandas as pd
import matplotlib.pyplot as plt

def obtener_tasa(de, a):
    url = f"https://api.exchangerate-api.com/v4/latest/{de}"
    response = requests.get(url)
    return response.json()["rates"][a]

def convertir_moneda(cantidad, de, a):
    tasa = obtener_tasa(de, a)
    return cantidad * tasa

def registrar_conversion(cantidad, de, a, resultado):
    conversion = {"Cantidad": cantidad, "De": de, "A": a, "Resultado": resultado}
    historial.append(conversion)
    df = pd.DataFrame(historial)
    df.to_csv("historial_conversiones.csv", index=False)

def graficar_historial():
    df = pd.read_csv("historial_conversiones.csv")
    df.plot(x="De", y="Resultado", kind="bar")
    plt.title("Historial de Conversiones")
    plt.show()

historial = []
cantidad = float(input("Cantidad: "))
de = input("Moneda de origen (ej. USD): ")
a = input("Moneda de destino (ej. EUR): ")

resultado = convertir_moneda(cantidad, de, a)
print(f"{cantidad} {de} son {resultado:.2f} {a}")
registrar_conversion(cantidad, de, a, resultado)
graficar_historial()
