
from nose.tools import assert_equal

from tests.assert_raises import assert_raises


def test_exception_ok():
    with assert_raises(ValueError):
        raise ValueError


def test_exception_as_ok():
    with assert_raises(ValueError) as e:
        raise ValueError('hello')
    assert_equal(str(e.exception), 'hello')


def test_exception_fails():
    try:
        with assert_raises(TypeError):
            raise ValueError
    except ValueError:
        pass


def test_exception_as_fails():
    try:
        with assert_raises(TypeError) as e:
            raise ValueError('hello')
    except ValueError:
        pass

