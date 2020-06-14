"""
Perform a Fourier transform frequency analysis of the sound of two different
musical instruments (record sound yourself via microphone and sound card on
a PC, on a mobile phone, or use wav-files made available from ourWeb pages).
Determine the frequency of the sound (fundamental tone) and find which tone
on the scale it corresponds to. State approximately how many harmonics you
find.

Lakukan analisis frekuensi Fourier transform dari dua suara alat musik
yang berbeda (rekam suara diri Anda melalui mikrofon dan kartu suara aktif
PC, di ponsel, atau gunakan file-file wav yang disediakan dari halaman Web kami).
Tentukan frekuensi suara (nada dasar) dan temukan nada mana yang sesuai dengan skala.
Nyatakan kira-kira berapa banyak harmonisa Anda Temukan.
"""

import sounddevice as sd
import soundfile as sf
import numpy as np
from matplotlib import pyplot as plt

# Importing sound file data and sample first
N = 64 * 1024
data1, sample1 = sf.read("piano1.wav", stop=N)
print("Piano 1 = ", data1)

# Importing sound file data and sample first
data2, sample2 = sf.read("piano2.wav", stop=N)
print("Piano 2 = ", data2)

# Playing sound
sd.play(data1, sample1)
sd.play(data2, sample2)

# The sound file is sample as a stereo signal
# Extracting only mono signal
mono_signal1 = data1[:, 0]
mono_signal2 = data2[:, 0]
print("mono signal 1 = ", mono_signal1)
print("mono signal 2 = ", mono_signal2)

# FFT
fft_spectrum1 = (1.0 / N) * np.fft.fft(mono_signal1)
fft_spectrum2 = (1.0 / N) * np.fft.fft(mono_signal2)
print("Fast Fourier Transform Piccolo Low = ", fft_spectrum1)
print("Fast Fourier Transform Piccolo High = ", fft_spectrum2)

# Frequency array for plotting
freq1 = (sample1 / 2) * np.linspace(0, 1, int(N / 2))
freq2 = (sample2 / 2) * np.linspace(0, 1, int(N / 2))
print("Frequency 1 = ", freq1)
print("Frequency 2 = ", freq2)

# plotting
plt.figure(1)
plt.title("FFT of Piano 1")
plt.plot(mono_signal1, 'r', linewidth=0.15)
plt.legend(mono_signal1)
plt.xlabel("Nilai Sample [N]")
plt.ylabel("Mono Signal Piano 1 [Hz]")
plt.grid(True)

plt.figure(2)
plt.plot(freq1, np.real(fft_spectrum1[0:int(len(fft_spectrum1) / 2)]),
         linewidth=0.5)
plt.text(77.0, 0.0006, 'fundamental tone [75 Hz]')
plt.xlabel("Frequency [Hz]")
plt.ylabel("Fourier spectrum, amplitude")
plt.grid(True)

plt.figure(3)
plt.title("FFT of Piano 2")
plt.plot(mono_signal2, 'c', linewidth=0.095)
plt.legend(mono_signal2)
plt.xlabel("Nilai Sample [N]")
plt.ylabel("Mono Signal Piano 2 [Hz]")
plt.grid(True)

plt.figure(4)
plt.plot(freq2, np.real(fft_spectrum2[0:int(len(fft_spectrum2) / 2)]),
         linewidth=0.5)
plt.text(120.0, 0.00123, 'fundamental tone [118 Hz]')
plt.xlabel("Frequency [Hz]")
plt.ylabel("Fourier spectrum, amplitude")
plt.grid(True)

plt.show()
