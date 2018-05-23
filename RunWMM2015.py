#!/usr/bin/env python
import numpy as np
import pywmm2015 as wmm
import pywmm2015.plots as plt
from matplotlib.pyplot import show


if __name__ == '__main__':
    lon,lat = np.meshgrid(np.arange(-180,180+10,10),np.arange(-90,90+10,10))

    mag = wmm.wmm(lat,lon,0,2015)

    plt.plotwmm(mag)

    show()