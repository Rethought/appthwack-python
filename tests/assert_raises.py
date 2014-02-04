import sys


class assert_raises_for_py26(object):
    evalue=None
    def __init__(self, wanted):
        self.wanted = wanted

    @property
    def exception(self):
        return self.evalue

    def __enter__(self):
        return self

    def __exit__(self, etype, evalue, tb):
        self.evalue = evalue
        if not issubclass(etype, self.wanted):
            raise etype(evalue)
        else:
            return True


if sys.version[:3] <= '2.6':
    assert_raises = assert_raises_for_py26
else:
    from nose.tools import assert_raises
