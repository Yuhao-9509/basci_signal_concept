#SNR is a value that represents the Signal-to-Noise Ratio , and a higher value is desirable. It can be calculated using SNR = P_signal / P_noise or in decibels as SNR_db = 10 * log10(P_signal / P_noise). 
#It's important to remember that P_signal represents the power of the signal, while P_noise represents the noise power. Therefore, P_signal is defined as E[signal^2], and P_noise is defined as E[noise^2]. 
#If the noise is white Gaussian noise, we can compute E[noise^2] = μ^2 + σ^2, where μ represents the mean and σ^2 represents the variance of the noise..
#Here's an example of how you can use the Signal-to-Noise Ratio (SNR) formula in Python.

import numpy as np
import matplotlib.pyplot as plt
# Define a function to add White Gaussian Noise (AWGN) to a signal
def add_awgn(signal, desired_snr_db):
  # Calculate the energy of the signal
    signal_energy  = np.sum(np.square(signal))/len(signal)
  # Calculate the noise energy based on SNR in decibels
    noise_energy = signal_energy/(10**((desired_snr_db/10)))
  # Generate white Gaussian noise
    noise = np.random.randn(len(signal)) * np.sqrt(noise_energy)
  # Add the signal and noise together
    AWAG_signal = signal + noise
    return AWAG_signal


t = np.linspace(0, 1, 1000)
signal = np.sin(2*np.pi*5*t)
# Plot the original signal
plt.subplot(211)
plt.plot(t, signal)
plt.title('Original Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')


# Add AWGN to the signal with 20 dB SNR
awgn_signal = add_awgn(signal, desired_snr_db=20)

# Plot the signal with added noise
plt.subplot(212)
plt.plot(t, awgn_signal)
plt.title('Signal with AWGN (20 dB SNR)')
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')

plt.tight_layout()
plt.show()
