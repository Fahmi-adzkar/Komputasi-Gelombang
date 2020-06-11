"""
Use inverse Fourier transformation to generate a simple sinusoid and play the sound on your computer.
Use the inbuilt sound or wavplay function (program snippet 1 a few pages ahead of this on indicates how).
Specifically, the following is recommended: Use the CD sampling rate fs = 44100Hz and 216 = 65536 points.
The values of the signal f must not exceed the interval [−1,+1].
Attempt to make sound with frequencies 100, 440, 1000 and 3000 Hz. You may want to
make a signal consisting of several simultaneous sinusoid too?
Remember to scale the total signal before using wavplay or sound.

Gunakan invers transformasi Fourier untuk menghasilkan sinusoid sederhana dan memainkannya di komputer Anda. Gunakan
suara inbuilt atau fungsi wavplay (program cuplikan 1 beberapa halaman di depan ini menunjukkan bagaimana caranya).
Secara khusus, berikut ini direkomendasikan: Gunakan laju pengambilan sampel CD fs = 44100Hz dan 2^16 = 65536 poin.
Nilai-nilai sinyal f tidak boleh melebihi interval [−1, + 1]. Mencoba untuk membuat suara dengan frekuensi 100, 440,
1000 dan 3000 Hz. Anda mungkin mau membuat sinyal yang terdiri dari beberapa sinusoid simultan juga? Ingat untuk
skala sinyal total sebelum menggunakan wavplay atau suara. """
import numpy as np
import matplotlib.pyplot as plt

Fs = 44100.0  # Sampling frequency
delta_t = 1.0 / Fs  # Time b/w each sample
N = 1024  # No of samples
t = np.arange(N) * delta_t  # Time array

print("Time = ", delta_t)
print("Time array = ", t)

# Synthesizing signal: sum of 3000 Hz sine and 3000 Hz cosine
sin_100_hz = np.sin(2 * np.pi * 100 * t)
print("Nilai Sin 100 Hz = ", sin_100_hz)

sin_440_hz = np.sin(2 * np.pi * 440 * t)
print("Nilai Sin 440 Hz = ", sin_440_hz)

sin_1000_hz = np.sin(2 * np.pi * 1000 * t)
print("Nilai Sin 1000 Hz = ", sin_1000_hz)

sin_3000_hz = np.sin(2 * np.pi * 3000 * t)
print("Nilai Sin 3000 Hz = ", sin_3000_hz)

x = sin_100_hz + sin_440_hz + sin_1000_hz + sin_3000_hz
print("Nilai Penjumlahan sinyal sin = ", x)

# Fast Fourier Transform
X = np.fft.fft(x, N) / N
print("Nilai Fast Fourier Transform = ", X)

# Invers Fourier Transform
Inv_X = np.fft.ifft(X)
print("Nilai Invers Fast Fourier Transform = ", Inv_X)

# Frequency array for plotting
freq = (Fs / 2) * np.linspace(0, 1, 512)
print("Nilai Frequency domain = ", freq)

# Plotting
plt.figure(1)
plt.title("Sinyal Sinus 100 Hz")
plt.plot(t, sin_100_hz)
plt.xlabel("Time [s]")
plt.ylabel("Sin 100 Hz")

plt.figure(2)
plt.title("Sinyal Sinus 440 Hz")
plt.plot(t, sin_440_hz)
plt.xlabel("Time [s]")
plt.ylabel("Sin 440 Hz")

plt.figure(3)
plt.title("Sinyal Sinus 1000 Hz")
plt.plot(t, sin_1000_hz)
plt.xlabel("Time [s]")
plt.ylabel("Sin 1000 Hz")

plt.figure(4)
plt.title("Sinyal Sinus 3000 Hz")
plt.plot(t, sin_3000_hz)
plt.xlabel("Time [s]")
plt.ylabel("Sin 3000 Hz")

plt.figure(5)
plt.title("Penjumlahan Sinyal Sinus")
plt.plot(x)
plt.xlabel("Nomer Sample [N]")
plt.ylabel("Sinus")

plt.figure(6)
plt.title("Time domain")
plt.plot(t, x)
plt.ylabel("Original signal, Hz")
plt.xlabel("Time [s]")

plt.figure(7)
plt.title("Frequency domain")
plt.plot(freq, 2 * np.real(X[0:round(N / 2)]))  # Half of Fourier spectrum
plt.ylabel("Fourier spectrum, amplitude")
plt.xlabel("Frequency [Hz]")

plt.figure(8)
plt.title("Frequency domain [Invers]")
plt.plot(freq, 2 * np.real(Inv_X[0:round(N / 2)]))  # Half of Fourier spectrum
plt.ylabel("Fourier spectrum, amplitude")
plt.xlabel("Frequency [Hz]")
plt.show()
