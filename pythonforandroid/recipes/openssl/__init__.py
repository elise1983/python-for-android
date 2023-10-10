from os.path import join

from pythonforandroid.recipe import Recipe
from pythonforandroid.util import current_directory
from pythonforandroid.logger import shprint
import sh


class OpenSSLRecipe(Recipe):

    version = '3'

    url_version = '3.1.3'
    '''the version used to download our libraries'''

    url = 'https://github.com/openssl/openssl/archive/refs/tags/{url_version}.1.3.tar.gz'

    built_libraries =
        'libcrypto{version}.so'.format(version=version): '.',
        'libssl{version}.so'.format(version=version): '.',
    }

    #@property
    #def versioned_url(self):
    #    if self.url is None:
    #        return None
    #    return self.url.format(url_version=self.url_version)

    def get_build_dir(self, arch):
        return join(
            self.get_build_container_dir(arch), self.name + self.version
        )

    def include_flags(self, arch):
        '''Returns a string with the include folders'''
        openssl_includes = join(self.get_build_dir(arch.arch), 'include')
        return (' -I' + openssl_includes +
                ' -I' + join(openssl_includes, 'internal') +
                ' -I' + join(openssl_includes, 'openssl'))

    def link_dirs_flags(self, arch):
        '''Returns a string with the appropriate `-L<lib directory>` to link
        with the openssl libs. This string is usually added to the environment
        variable `LDFLAGS`'''
        return ' -L' + self.get_build_dir(arch.arch)

    def link_libs_flags(self):
        '''Returns a string with the appropriate `-l<lib>` flags to link with
        the openssl libs. This string is usually added to the environment
        variable `LIBS`'''
        return ' -lcrypto{version} -lssl{version}'.format(version=self.version)

    def link_flags(self, arch):
        '''Returns a string with the flags to link with the openssl libraries
        in the format: `-L<lib directory> -l<lib>`'''
        return self.link_dirs_flags(arch) + self.link_libs_flags()

    def get_recipe_env(self, arch=None):
        env = super().get_recipe_env(arch)
        env['OPENSSL_VERSION'] = self.version
        env['MAKE'] = 'make'  # This removes the '-j5', which isn't safe
        env['CC'] = 'clang'
        env['ANDROID_NDK_HOME'] = self.ctx.ndk_dir
        return env

    def select_build_arch(self, arch):
        aname = arch.arch
        if 'arm64' in aname:
            return 'android-arm64'
        if 'v7a' in aname:
            return 'android-arm'
        if 'arm' in aname:
            return 'android'
        if 'x86_64' in aname:
            return 'android-x86_64'
        if 'x86' in aname:
            return 'android-x86'
        return 'linux-armv4'

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # sh fails with code 255 trying to execute ./Configure
            # so instead we manually run perl passing in Configure
            perl = sh.Command('perl')
            buildarch = self.select_build_arch(arch)
            config_args = [
                'shared',
                'no-dso',
                'no-asm',
                buildarch,
                '-D__ANDROID_API__={}'.format(self.ctx.ndk_api),
            ]
            shprint(perl, 'Configure', *config_args, _env=env)
            self.apply_patch('disable-sover.patch', arch.arch)

            shprint(sh.make, 'build_libs', _env=env)


recipe = OpenSSLRecipe()
