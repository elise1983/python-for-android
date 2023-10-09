from pythonforandroid.recipe import CppCompiledComponentsPythonRecipe


class EnamlRecipe(CppCompiledComponentsPythonRecipe):
    site_packages_name = 'enaml'
    version = '1.16.1'
    url = 'https://github.com/nucleic/enaml/archive/{version}.zip'
    patches = ['0001-Update-setup.py.patch']  # Remove PyQt dependency
    depends = ['setuptools', 'atom', 'kiwisolver']


recipe = EnamlRecipe()
