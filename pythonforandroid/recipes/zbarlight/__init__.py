from os.path import join
from pythonforandroid.recipe import PythonRecipe


class ZBarLightRecipe(PythonRecipe):

    version = '3.0'

    url = 'https://github.com/Polyconseil/zbarlight/archive/{version}.tar.gz'  # noqa

    call_hostpython_via_targetpython = False

    depends = ['setuptools', 'libzbar']

    def get_recipe_env(self, arch=None, with_flags_in_cc=True):
        env = super().get_recipe_env(arch, with_flags_in_cc)
        libzbar = self.get_recipe('libzbar', self.ctx)
        libzbar_dir = libzbar.get_build_dir(arch.arch)
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir(arch.arch)
        env['CFLAGS'] += ' -I' + join(libzbar_dir, 'include')
        env['LDFLAGS'] += ' -L' + join(libzbar_dir, 'zbar', '.libs')
        env['LIBS'] = env.get('LIBS', '') + ' -landroid -lzbar'
        return env


recipe = ZBarLightRecipe()
