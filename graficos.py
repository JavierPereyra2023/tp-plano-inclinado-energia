import pandas as pd
import matplotlib.pyplot as plt


# Datos de ejemplo ficticios.
# El profesor puede modificar estos valores por los resultados reales del curso.
datos = pd.DataFrame(
    {
        "Pelotita": ["Vidrio", "Goma", "Telgopor", "Plastico", "Metal"],
        "Superficie": ["Carton liso", "Tela", "Lija fina", "Goma eva", "Plastico"],
        "Masa_kg": [0.018, 0.045, 0.006, 0.020, 0.065],
        "Altura_m": [0.35, 0.35, 0.35, 0.35, 0.35],
        "Distancia_m": [1.20, 1.20, 1.20, 1.20, 1.20],
        "Tiempo_prom_s": [1.24, 1.43, 1.78, 1.62, 1.18],
        "Emi_J": [0.0617, 0.1544, 0.0206, 0.0686, 0.2229],
        "Emf_J": [0.0084, 0.0158, 0.0041, 0.0055, 0.0336],
    }
)

datos["Velocidad_media_m_s"] = datos["Distancia_m"] / datos["Tiempo_prom_s"]
datos["Delta_Em_J"] = datos["Emi_J"] - datos["Emf_J"]
datos["Perdida_porcentaje"] = (datos["Delta_Em_J"] / datos["Emi_J"]) * 100


def aplicar_estilo(titulo, eje_x, eje_y):
    plt.title(titulo, fontsize=13, weight="bold")
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    plt.grid(axis="y", alpha=0.25)
    plt.tight_layout()


plt.figure(figsize=(9, 5))
plt.bar(datos["Pelotita"], datos["Velocidad_media_m_s"], color="#20a8d8")
aplicar_estilo(
    "Velocidad media para cada pelotita",
    "Pelotita",
    "Velocidad media (m/s)",
)
plt.savefig("assets/grafico_velocidad_media.png", dpi=180)
plt.close()

plt.figure(figsize=(9, 5))
x = range(len(datos))
plt.bar([i - 0.18 for i in x], datos["Emi_J"], width=0.36, label="Emi", color="#0f6fb2")
plt.bar([i + 0.18 for i in x], datos["Emf_J"], width=0.36, label="Emf", color="#0f9f80")
plt.xticks(list(x), datos["Pelotita"])
plt.legend()
aplicar_estilo(
    "Energia mecanica inicial y final",
    "Pelotita",
    "Energia mecanica (J)",
)
plt.savefig("assets/grafico_energia_mecanica.png", dpi=180)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(datos["Superficie"], datos["Perdida_porcentaje"], color="#f28c28")
plt.xticks(rotation=20, ha="right")
aplicar_estilo(
    "Porcentaje de perdida de energia segun superficie",
    "Superficie del plano",
    "Perdida de energia (%)",
)
plt.savefig("assets/grafico_perdida_energia.png", dpi=180)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(datos["Superficie"], datos["Tiempo_prom_s"], color="#0fb7a5")
plt.xticks(rotation=20, ha="right")
aplicar_estilo(
    "Tiempo promedio segun superficie del plano",
    "Superficie del plano",
    "Tiempo promedio (s)",
)
plt.savefig("assets/grafico_tiempo_superficie.png", dpi=180)
plt.close()

print("Graficos generados en la carpeta assets/")
