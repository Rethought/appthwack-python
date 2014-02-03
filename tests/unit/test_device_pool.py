from nose.tools import assert_equal

from appthwack.appthwack import AppThwackDevicePool


def test__str__():
    d = AppThwackDevicePool(name='devious', id=432)
    assert_equal(str(d), 'devicepool/432')
