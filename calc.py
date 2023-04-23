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

# Aplicar la Transformada de Fourier a la señal
fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft_signal), 1/fs)

# Plotear la señal y su espectro de frecuencias
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Señal compuesta por dos frecuencias')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_signal))
plt.title('Espectro de frecuencias de la señal')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
