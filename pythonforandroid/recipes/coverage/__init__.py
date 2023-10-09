from pythonforandroid.recipe import PythonRecipe


class CoverageRecipe(PythonRecipe):

    version = '7.3.2'

    url = 'https://files.pythonhosted.org/packages/57/44/ecd5442163c53f333bfcd2e7f428457a68b008a4b65d436a64b1db362451/coverage-7.3.2.tar.gz'

    depends = ['hostpython3', 'setuptools']



    site_packages_name = 'coverage'

    call_hostpython_via_targetpython = False


recipe = CoverageRecipe()
