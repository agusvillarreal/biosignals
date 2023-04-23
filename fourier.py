import numpy as np
import matplotlib.pyplot as plt

# Crear una señal de ejemplo
t = np.linspace(0, 1, 1000)
f = 5
signal = np.sin(2 * np.pi * f * t)

# Calcular la FFT
fft_result = np.fft.fft(signal)

# Calcular las frecuencias
freqs = np.fft.fftfreq(len(fft_result))

# Plotear la señal original y su FFT
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Señal Original')

plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(fft_result))
plt.title('FFT')
plt.xlim(0, 5)  # Ajusta el rango de frecuencia visible en el gráfico

plt.show()
