from pythonforandroid.recipe import PythonRecipe


class SixRecipe(PythonRecipe):
    version = '1.16.0'
    url = 'https://pypi.python.org/packages/source/s/six/six-{version}.tar.gz'
    depends = ['setuptools']


recipe = SixRecipe()
