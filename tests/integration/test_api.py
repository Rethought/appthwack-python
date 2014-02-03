import os

from nose.tools import assert_raises, assert_equal

from appthwack import AppThwackApi, AppThwackApiError
from appthwack.appthwack import AppThwackProject, AppThwackFile

from .utils import no_env

api = None


def setup():
    """ensure that there is an API KEY and set the (module) global variable api
    """
    try:
        os.environ['APPTHWACK_API_KEY']
        global api
        api = AppThwackApi()
    except KeyError:
        assert False, ' No APPTHWACK_API_KEY environment variable set!'


def test_constructor_fails_if_no_env_var_set():
    with no_env('APPTHWACK_API_KEY'):
        with assert_raises(ValueError) as e:
            AppThwackApi()
    assert_equal(str(e.exception), 'AppThwack API key must be provided.')

# --- project tests: these are only valuable if there exists at least one
#     project

def test_projects():
    for p in api.projects():
        assert isinstance(p, AppThwackProject)


def test_project():
    projects = api.projects()
    if projects:
        project = projects[0]
        p = api.project(name=project.name)
        assert p.name == project.name


class Test_upload(object):

    def setup(self):
        self.valid_path = os.path.join(os.path.dirname(__file__), 'small.apk')

    def test_fails_if_file_has_no_extension(self):
        with assert_raises(ValueError) as e:
            api.upload('no_file_ext')
        assert_equal(str(e.exception),'Path must contain a file extension.')

    def test_ok_with_name_ok(self):
        res = api.upload(self.valid_path, name='fred.apk')
        assert isinstance(res, AppThwackFile)
        assert_equal (str(res), 'file/%s' % res.file_id)

    def test_opk_without_name(self):
        res = api.upload(self.valid_path)
        assert isinstance(res, AppThwackFile)

    def test_fails_if_filepath_is_invalid(self):
        with assert_raises(IOError):
            api.upload('/path/to/junk.apk')

    def test_fails_if_file_ok_but_name_has_no_extension(self):
        with assert_raises(AppThwackApiError) as e:
            api.upload(self.valid_path, name='fred')
        assert 'Unsupported file type' in str(e.exception), str(e.exception)
