from pythonforandroid.recipe import PythonRecipe


class PyamlRecipe(PythonRecipe):
    version = "23.9.7"
    url = 'https://pypi.python.org/packages/source/p/pyaml/pyaml-{version}.tar.gz'
    depends = ["setuptools"]
    site_packages_name = 'yaml'
    call_hostpython_via_targetpython = False


recipe = PyamlRecipe()
