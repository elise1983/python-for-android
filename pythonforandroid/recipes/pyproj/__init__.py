from pythonforandroid.recipe import CythonRecipe


class PyProjRecipe(CythonRecipe):
    version = '3.6.1'
    url = 'https://github.com/pyproj4/pyproj/archive/v{version}rel.zip'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = PyProjRecipe()
