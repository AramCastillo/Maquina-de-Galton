import numpy as np
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_niveles):
    resultados = np.zeros(num_niveles + 1, dtype=int)

    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            # Decidir aleatoriamente hacia dónde caerá la canica (izquierda o derecha)
            if np.random.rand() < 0.5:
                posicion += 1
        resultados[posicion] += 1

    return resultados

def graficar_histograma(resultados):
    niveles = np.arange(len(resultados))
    plt.bar(niveles, resultados, color='blue', alpha=0.7)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de Máquina de Galton')
    plt.show()

# Simular la máquina de Galton con 3000 canicas y 12 niveles
num_canicas = 3000
num_niveles = 12
resultados_simulacion = simular_maquina_galton(num_canicas, num_niveles)

# Graficar el histograma de los resultados
graficar_histograma(resultados_simulacion)
