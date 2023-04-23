import numpy as np
import time

# Parámetros de la señal
fs = 8000  # Frecuencia de muestreo (Hz)
duration = 1  # Duración de la señal (segundos)
t = np.arange(0, duration, 1/fs)  # Vector de tiempo

# Generar la señal compuesta por dos frecuencias
f1 = 440  # Frecuencia 1 (Hz)
f2 = 880  # Frecuencia 2 (Hz)
signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Número de puntos en la señal
N = len(signal)

# Función para calcular la DFT utilizando el método directo
def dft_direct(x):
    N = len(x)
    dft = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            dft[n] += x[k] * np.exp(-2j * np.pi * k * n / N)
    return dft

# Calcular la DFT usando el método directo y medir el tiempo de cálculo
start_time = time.time()
dft_signal_direct = dft_direct(signal)
direct_time = time.time() - start_time

# Calcular la DFT usando la FFT y medir el tiempo de cálculo
start_time = time.time()
dft_signal_fft = np.fft.fft(signal)
fft_time = time.time() - start_time

# Comparar los tiempos de cálculo
print(f"Tiempo de cálculo de la DFT (método directo): {direct_time:.6f} segundos")
print(f"Tiempo de cálculo de la DFT (FFT): {fft_time:.6f} segundos")
