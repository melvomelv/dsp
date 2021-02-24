import numpy as np
import scipy.signal
import matplotlib.pyplot as plt


class filters: 

    def LPF_ham(self, fs = 'Sampling Rate', fc = 'Cutoff Frequency', N = 'Filter Length, Coefficients'):

        #compute Sinc Filter
        h = np.sinc(2* fc/fs * (np.arange(N) - (N-1)/2))

        #apply window of length N, these are the filter coefficients
        h *= np.hamming(N)

        #Normalze, unity gain
        h /= np.sum(h)

        return h

    def LPF_black(self, fs = 'Sampling Rate', fc = 'Cutoff Frequency', N = 'Filter Length, Coefficients'):

        h = np.sinc(2* fc/fs * (np.arange(N) - (N-1)/2))

        #apply window of length N, these are the filter coefficients
        h *= np.blackman(N)

        #Normalze, unity gain
        h /= np.sum(h)

        return h

    def LPF_kaiser(self, fs = 'Sampling Rate', fc = 'Cutoff Frequency', N = 'Filter Length, Coefficients', beta = 'Kaiser Window Beta'):

        #calculate Sinc Filter
        h = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2))

        # Apply window.
        h *= np.kaiser(N, beta)

        # Normalize to get unity gain.
        h /= np.sum(h)

        return h

    def LPF_rect(self, fs = 'Sampling Rate', fc = 'Cutoff Frequency', N = 'Filter Length, Coefficients'):

        #calculate Sinc Filter
        h = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2))

        # Normalize to get unity gain.
        h /= np.sum(h)

        return h