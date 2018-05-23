import numpy as np
from pathlib import Path
import xarray
import ctypes as ct

R = Path(__file__).parents[1] / 'bin'

libwmm = ct.cdll.LoadLibrary(str(R/'libwmm15.so'))

def wmm(glats:float, glons:float, alt_km:float, yeardec:float) -> xarray.Dataset:

    glats = np.atleast_2d(glats).astype(float) # to coerce all else to float64
    glons = np.atleast_2d(glons)

    assert glats.shape == glons.shape

    mag = xarray.Dataset(coords={'glat':glats[:,0],'glon':glons[0,:]})
    north = np.empty(glats.size)
    east = np.empty(glats.size)
    down = np.empty(glats.size)
    total = np.empty(glats.size)
    decl = np.empty(glats.size)
    incl = np.empty(glats.size)

    for i,(glat, glon) in enumerate(zip(glats.ravel(),glons.ravel())):

        x=ct.c_double()
        y=ct.c_double()
        z=ct.c_double()
        T = ct.c_double()
        D = ct.c_double()
        I = ct.c_double()

        ret = libwmm.wmmsub(ct.c_double(glat),
                              ct.c_double(glon),
                              ct.c_double(alt_km),
                              ct.c_double(yeardec),
                              ct.byref(x), ct.byref(y), ct.byref(z),
                              ct.byref(T), ct.byref(D), ct.byref(I))

        assert ret==0

        north[i] = x.value
        east[i] = y.value
        down[i] = z.value
        total[i] = T.value
        decl[i] = D.value
        incl[i] = I.value

    mag['north'] = (('glat','glon'),north.reshape(glats.shape))
    mag['east']  = (('glat','glon'),east.reshape(glats.shape))
    mag['down']  = (('glat','glon'),down.reshape(glats.shape))
    mag['total']  = (('glat','glon'),total.reshape(glats.shape))
    mag['incl']  = (('glat','glon'),incl.reshape(glats.shape))
    mag['decl']  = (('glat','glon'),decl.reshape(glats.shape))

    mag.attrs['time'] = yeardec

    return mag