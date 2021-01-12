import numpy as np
import scipy.signal as sig
import math


PI2 = math.pi * 2


def pad_width(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 0)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

class processing:

    def conv_1D(self, signal, h): #cyclic convolution
        signal_l = np.size(signal)
        h_l = np.size(h)
        signal = np.pad(signal, (0, h_l - 1), pad_width)
        h = np.pad(h, (0, signal_l - 1), pad_width)
        signal = np.fft.ifft((np.fft.fft(signal)) * (np.fft.fft(h)))
        return signal

    def conv_2d(self, image, filter): #cyclic convolution

        #filter and image dimensions
        #r, c = image.shape
        filter_l = filter.shape[0]
        image_r = image.shape[0]
        image_c = image.shape[1]

        #pad image and filter
        image = np.pad(image, ((0, filter_l-1), (0, filter_l-1)), pad_width)
        filter = np.pad(filter, ((0, image_r - 1), (0, image_c - 1)), pad_width)

        image = np.fft.fft2(image)
        image = np.fft.fftshift(image)
        filter = np.fft.fft2(filter)
        filter = np.fft.fftshift(filter)
        image = filter * image
        image = np.fft.ifftshift(image)
        image = np.fft.ifft2(image)

        return image


    def sobel(self, image): #uses the FFT to significantly improve processing time

        x_kernal = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]))
        y_kernal = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1]))

        image_x = self.conv_2d(image, x_kernal)
        image_y = self.conv_2d(image, y_kernal)

        # calculate mag at each pixel
        image = np.abs((image_x) ** 2 + (image_y) ** 2)

        #intensity rescaling, may not be necessary depending on input color intensity
        #image = skimage.exposure.rescale_intensity(image, in_range=(0, 255))
        #image = (image * 255).astype('uint8')

        return image


    def binary_search(value, array, left=0):

        if len(array) == 0:
            return -1

        mid_point = (len(array) - 1) // 2

        if array[mid_point] == value:
            return mid_point + left

        elif array[mid_point] > value:
            return binary_search(value, array[:mid_point], left)

        else:
            return binary_search(value, array[mid_point + 1:], left + mid_point + 1)




class Signal:

    def __init__(self, freq, amp, offset, in_array):
        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.in_array = in_array

    def cosine(self):
        return self.amp * np.cos(PI2 * self.freq * self.in_array - self.offset)

    def sine(self):
        return self.amp * np.sin(PI2 * self.freq * self.in_array - self.offset)

    def squarewave(self):
        return signal.square(2 * np.pi * self.freq * self.in_array)

    def triangle_wave(self):
        return signal.sawtooth(2* np.pi* self.freq * self.in_array, .5)

    def sawtooth(self):
        return signal.sawtooth(2*np.pi*self.freq * self.in_array)

    def complex_signal(self, amp, freq):
        phase = PI2 * freq
        ys = amp * np.exp(1j * phase)
        return ys

    def synthesis_complex(self, amps, freqs, ts):
        args = np.outer(ts, freqs)
        M = np.exp(1j * PI2 * args)
        ys = np.dot(M, amps)
        return ys

    def DFT_matrix_synthesis(self, N):
        ts = np.arange(N) / N
        fs = np.arange(N)
        args = np.outer(ts, fs)
        M = np.exp(1j * PI2 * args)
        return M

    def actual_DFT(self, ys):
        N = len(ys)
        M = self.DFT_matrix_synthesis(N)
        amps = M.conj().transpose().dot(ys)
        return amps

    def cos_synthesis(self, amps, freqs, ts):
        args = np.outer(ts, freqs)
        M = np.cos(PI2*args)
        ys = np.dot(M,amps)
        return ys

    def sine_synthesis(self, amps, freqs, ts):
        args = np.outer(ts, freqs)
        M = np.sin(PI2*args)
        ys = np.dot(M, amps)
        return ys


