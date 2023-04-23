import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 8000  # Frecuencia de muestreo (Hz)
duration = 1  # Duración de la señal (segundos)
t = np.arange(0, duration, 1/fs)  # Vector de tiempo

# Generar la señal de audio original
f = 440  # Frecuencia de la señal (Hz)
original_signal = np.sin(2 * np.pi * f * t)

# Agregar ruido aleatorio a la señal
noise = np.random.normal(0, 0.5, len(t))
noisy_signal = original_signal + noise

# Aplicar la transformada de Fourier
fft_noisy_signal = np.fft.fft(noisy_signal)

# Filtrar el ruido
threshold = 50
fft_filtered_signal = np.copy(fft_noisy_signal)
fft_filtered_signal[np.abs(fft_filtered_signal) < threshold] = 0

# Aplicar la transformada de Fourier inversa
filtered_signal = np.fft.ifft(fft_filtered_signal)

# Plotear las señales
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, noisy_signal, label='Señal con ruido')
plt.plot(t, original_signal, label='Señal original', linestyle='dashed')
plt.legend()
plt.title('Señal original y señal con ruido')

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal.real, label='Señal filtrada')
plt.plot(t, original_signal, label='Señal original', linestyle='dashed')
plt.legend()
plt.title('Señal original y señal filtrada')

plt.show()
