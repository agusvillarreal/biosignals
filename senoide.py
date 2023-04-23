import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 8000  # Frecuencia de muestreo (Hz)
duration = 1  # Duración de la señal (segundos)
t = np.arange(0, duration, 1/fs)  # Vector de tiempo

# Generar la señal senoidal
f = 440  # Frecuencia de la señal (Hz)
original_signal = np.sin(2 * np.pi * f * t)

# Agregar ruido aleatorio a la señal
noise = np.random.normal(0, 0.5, len(t))
noisy_signal = original_signal + noise

# Aplicar la transformada de Fourier
fft_noisy_signal = np.fft.fft(noisy_signal)
frequencies = np.fft.fftfreq(len(fft_noisy_signal), 1/fs)

# Plotear las señales
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, noisy_signal, label='Señal con ruido')
plt.plot(t, original_signal, label='Señal original', linestyle='dashed')
plt.legend()
plt.title('Señal original y señal con ruido')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_noisy_signal), label='Espectro de frecuencias')
plt.legend()
plt.title('Espectro de frecuencias de la señal con ruido')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
