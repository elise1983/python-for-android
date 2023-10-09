from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class Argon2Recipe(CompiledComponentsPythonRecipe):
    version = '23.1.0'
    url = 'https://github.com/hynek/argon2-cffi/archive/{version}.tar.gz'
    depends = ['setuptools', 'cffi']
    call_hostpython_via_targetpython = False
    build_cmd = 'build'

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['ARGON2_CFFI_USE_SSE2'] = '0'
        return env


recipe = Argon2Recipe()
