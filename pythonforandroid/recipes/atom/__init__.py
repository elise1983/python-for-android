from pythonforandroid.recipe import CppCompiledComponentsPythonRecipe


class AtomRecipe(CppCompiledComponentsPythonRecipe):
    site_packages_name = 'atom'
    version = '0.10.3'
    url = 'https://github.com/nucleic/atom/archive/{version}.zip'
    depends = ['setuptools']


recipe = AtomRecipe()
