#!/usr/bin/env python
import datetime
import pytest
from pytest import approx
from sciencedates import datetime2yeardec
import wmm2015 as wmm


def test_wmm2015():
    dt = datetime.datetime(2012, 7, 12, 12)

    mag = wmm.wmm(65, 85, 0, datetime2yeardec(dt))

    assert mag.north.item() == approx(9215.692665)
    assert mag.east.item() == approx(2516.0058789)
    assert mag.down.item() == approx(59708.529371)
    assert mag.total.item() == approx(60467.906831)

    assert mag.incl.item() == approx(80.910090)
    assert mag.decl.item() == approx(15.27036)


if __name__ == "__main__":
    pytest.main(["-x", __file__])
