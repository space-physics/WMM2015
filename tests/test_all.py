#!/usr/bin/env python
import datetime
import numpy as np
#
import pywmm2015 as wmm

def test_wmm2015():
    dt = datetime.datetime(2012,7,12,12)

    mag = wmm.wmm(65,85,0,2012.5)

    np.testing.assert_allclose(mag.north,9216.865031)
    np.testing.assert_allclose(mag.east, 2516.406981)
    np.testing.assert_allclose(mag.down, 59708.029303)
    np.testing.assert_allclose(mag.total, 60467.608422)

    np.testing.assert_allclose(mag.incl, 80.908858)
    np.testing.assert_allclose(mag.decl, 15.270835)

if __name__ == '__main__':
    np.testing.run_module_suite()