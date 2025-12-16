import numpy as np
from scipy.signal import convolve2d

def gaussian_kernel(size=9, sigma=1.0):
    ax = np.arange(-(size//2), size//2+1)
    xx,yy = np.meshgrid(ax,ax)
    k = np.exp(-(xx**2+yy**2)/(2*sigma**2))
    return k/np.sum(k)

class DegradationOperator:
    def __init__(self, s, kernel):
        self.s=s
        self.k = kernel
        self.kT = np.flipud(np.fliplr(kernel))

    def apply(self,x):
        blurred = convolve2d(x,self.k,mode='same',boundary='wrap')
        return blurred[::self.s,::self.s]

    def adjoint(self,y):
        hr = np.zeros((y.shape[0]*self.s, y.shape[1]*self.s))
        hr[::self.s,::self.s] = y
        return convolve2d(hr,self.kT,mode='same',boundary='wrap')
