
from nose.tools import assert_raises, assert_equal

from appthwack.appthwack import (AppThwackProject, AppThwackAndroidProject,
                                 AppThwackIOSProject, AppThwackWebProject,
                                 ANDROID_PROJECT, WEB_PROJECT, IOS_PROJECT
                                )

class TestConstructor():

    def test_not_all_attributes_set(self):
        with assert_raises(ValueError) as e:
            AppThwackProject(name='android', url='myurl')
        assert_equal(str(e.exception), 'Invalid decoded json (for AppThwackAndroidProject).')

    def test_default_type_id(self):
        p = AppThwackProject(name='anyandroid', id=12345, url='a-url')
        assert isinstance(p, AppThwackAndroidProject), type(p)
        assert p.id == 12345
        assert p.name == 'anyandroid'
        assert p.url == 'a-url'

    def test_android(self):
        p = AppThwackProject(name='anyandroid', id=12345, url='a-url',
                             project_type_id=ANDROID_PROJECT)
        assert isinstance(p, AppThwackAndroidProject), type(p)
        assert p.id == 12345
        assert p.name == 'anyandroid'
        assert p.url == 'a-url'

    def test_ios(self):
        p = AppThwackProject(name='anyapple', id=12346, url='i-url',
                             project_type_id=IOS_PROJECT)
        assert isinstance(p, AppThwackIOSProject), type(p)
        assert p.id == 12346
        assert p.name == 'anyapple'
        assert p.url == 'i-url'

    def test_web(self):
        p = AppThwackProject(name='anyweb', id=12347, url='w-url',
                             project_type_id=WEB_PROJECT)
        assert isinstance(p, AppThwackWebProject), type(p)
        assert p.id == 12347
        assert p.name == 'anyweb'
        assert p.url == 'w-url'

    def test_invalid_project_type_id(self):
        with assert_raises(KeyError):
            AppThwackProject(name='invalid', url='myurl', id=123, project_type_id=0)
        with assert_raises(KeyError):
            AppThwackProject(name='invalid', url='myurl', id=123, project_type_id=4)
