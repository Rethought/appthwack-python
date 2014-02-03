from nose.tools import assert_equal

from appthwack.appthwack import (AppThwackDevicePool,
                                )

from .utils import get_valid_api, RunSetupError

api= None
project=None
def setup():
    '''ensure that there is an API KEY and set the (module) global variable api
    '''
    global api
    api = get_valid_api()


    projects = api.projects()
    if projects:
        global project
        project = projects[0]
    else:
        raise RunSetupError('No projects are available to test devices')


# --- device tests: these are only valuable if there exists at least one
#     project, and that project has at leat one device

def test_device_pools():
    ds = project.device_pools()
    for d in ds:
        assert isinstance(d, AppThwackDevicePool)


def test_device_pool():
    ds = project.device_pools()
    if ds:
        device_pool = ds[0]
        d = project.device_pool(name=device_pool.name)
        assert_equal(d.name, device_pool.name)
        assert_equal(d.id, device_pool.id)
