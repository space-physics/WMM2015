from pytest import approx

import wmm2015 as wmm


def test_wmm2015():
    mag = wmm.wmm(65, 85, alt_km=0, yeardec=2012.52868852459)

    assert mag.north.item() == approx(9215.692665)
    assert mag.east.item() == approx(2516.0058789)
    assert mag.down.item() == approx(59708.529371)
    assert mag.total.item() == approx(60467.906831)

    assert mag.incl.item() == approx(80.910090)
    assert mag.decl.item() == approx(15.27036)
