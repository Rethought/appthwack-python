import os
from contextlib import contextmanager


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


