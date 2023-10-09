from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class UJsonRecipe(CompiledComponentsPythonRecipe):
    version = '5.8.0
    url = 'https://pypi.python.org/packages/source/u/ujson/ujson-{version}.tar.gz'
    depends = []


recipe = UJsonRecipe()
