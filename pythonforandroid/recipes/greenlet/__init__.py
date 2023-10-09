from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class GreenletRecipe(CompiledComponentsPythonRecipe):
    version = '3.0.0'
    url = 'https://pypi.python.org/packages/source/g/greenlet/greenlet-{version}.tar.gz'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = GreenletRecipe()
