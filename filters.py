import numpy as np


class filters:
    
    def low_pass_hamming(cutoff, N):
  
        n = np.arange(N)
        filt = 2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.hamming(N)
    
        return filt*window

    def low_pass_bartlett(cutoff, N):
    
        n = np.arange(N)
        filt = 2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.bartlett(N)
    
        return filt*window

    def low_pass_blackman(cutoff, N):
    
        n = np.arange(N)
        filt = 2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.blackman(N)
    
        return filt*window

    def low_pass_hanning(cutoff, N):
        
        n = np.arange(N)
        filt = 2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.hanning(N)
    
        return filt*window

    def high_pass_hamming(cutoff, N):

        n = np.arange(N)
        filt = np.sinc(n-N/2)-2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.hamming(N)
    
        return filt*window

    def high_pass_bartlett(cutoff, N):
 
        n = np.arange(N)
        filt = np.sinc(n-N/2)-2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.bartlett(N)
    
        return filt*window

    def high_pass_blackman(cutoff, N):
  
        n = np.arange(N)
        filt = np.sinc(n-N/2)-2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.blackman(N)
    
        return filt*window

    def high_pass_hanning(cutoff, N):

        n = np.arange(N)
        filt = np.sinc(n-N/2)-2*cutoff*np.sinc(2*cutoff*(n-N/2))
        window = np.hanning(N)
    
        return filt*window

    def band_pass_filter(hpf, lpf):
        return np.convolve(hpf, lpf)

    def band_stop_filter(lpf, hpf):
        return lpf+hpf
