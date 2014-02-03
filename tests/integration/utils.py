import os
from contextlib import contextmanager

from appthwack import AppThwackApi


@contextmanager
def set_env(env_name, env_value):
    try:
        orig_value = os.environ[env_name]
    except KeyError:
        orig_value = None
    os.environ[env_name] = env_value
    try:
        yield
    finally:
        if orig_value is not None:
            os.environ[env_name] = orig_value


@contextmanager
def no_env(env_name):
    try:
        orig_value = os.environ[env_name]
        del os.environ[env_name]
    except KeyError:
        orig_value = None
    try:
        yield
    finally:
        if orig_value is not None:
            os.environ[env_name] = orig_value


class RunSetupError(Exception):
    pass


def get_valid_api():
    '''ensure that there is an API KEY and set the (module) global variable api
    '''
    if 'APPTHWACK_API_KEY'in os.environ:
        return AppThwackApi()
    else:
        print sorted(os.environ.iterkeys())
        raise RunSetupError(' No APPTHWACK_API_KEY environment variable set!')
