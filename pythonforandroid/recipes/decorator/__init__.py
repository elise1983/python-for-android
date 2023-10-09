from pythonforandroid.recipe import PythonRecipe


class DecoratorPyRecipe(PythonRecipe):
    version = '4.2.2'
    url = 'https://github.com/micheles/decorator/archive/{version}.tar.gz'
    depends = ['setuptools']
    site_packages_name = 'decorator'
    call_hostpython_via_targetpython = False


recipe = DecoratorPyRecipe()
