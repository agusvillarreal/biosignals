import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 8000  # Frecuencia de muestreo (Hz)
duration = 1  # Duración de la señal (segundos)
t = np.arange(0, duration, 1/fs)  # Vector de tiempo

# Generar la señal compuesta por dos frecuencias
f1 = 440  # Frecuencia 1 (Hz)
f2 = 880  # Frecuencia 2 (Hz)
signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Aplicar la Transformada Discreta de Fourier (DFT) a la señal
N = len(signal)  # Número de puntos en la señal
dft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(N, 1/fs)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(frequencies, np.abs(dft_signal), color='white')

# Configurar el fondo transparente y las líneas en blanco
fig.patch.set_alpha(0.0)  # Fondo transparente del gráfico
ax.patch.set_alpha(0.0)  # Fondo transparente del área de trazado
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='both', colors='white')

# Configurar el título y las etiquetas de los ejes
ax.set_title('Espectro de frecuencias de la señal (DFT)', color='white')
ax.set_xlabel('Frecuencia (Hz)')
ax.set_ylabel('Amplitud')

# Mostrar el gráfico
plt.show()
