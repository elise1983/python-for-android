from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class RegexRecipe(CompiledComponentsPythonRecipe):
    name = 'regex'
    version = '2023.10.3'
    url = 'https://pypi.python.org/packages/source/r/regex/regex-{version}.tar.gz'  # noqa

    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = RegexRecipe()
