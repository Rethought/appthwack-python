from nose.tools import assert_equal

from appthwack.appthwack import AppThwackFile


def test__str__():
    fil = AppThwackFile(file_id=4312)
    assert_equal(str(filgit), 'file/4312')
