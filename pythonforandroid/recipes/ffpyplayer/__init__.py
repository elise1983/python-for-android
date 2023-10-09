from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.toolchain import Recipe
from os.path import join


class FFPyPlayerRecipe(CythonRecipe):
    version = '4.5.1'
    url = 'https://files.pythonhosted.org/packages/b9/e8/f99fa2fe4abbdcc2f80d4b24cf65f3a049566e2cb61ec099d80ac51f367d/ffpyplayer-4.5.1.tar.gz'
    depends = ['python3', 'sdl2', 'ffmpeg']
    opt_depends = ['openssl', 'ffpyplayer_codecs']

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super().get_recipe_env(arch)

        build_dir = Recipe.get_recipe('ffmpeg', self.ctx).get_build_dir(arch.arch)
        env["FFMPEG_INCLUDE_DIR"] = join(build_dir, "include")
        env["FFMPEG_LIB_DIR"] = join(build_dir, "lib")

        env["SDL_INCLUDE_DIR"] = join(self.ctx.bootstrap.build_dir, 'jni', 'SDL', 'include')
        env["SDL_LIB_DIR"] = join(self.ctx.bootstrap.build_dir, 'libs', arch.arch)

        env["USE_SDL2_MIXER"] = '1'

        # ffpyplayer does not allow to pass more than one include dir for sdl2_mixer (and ATM is
        # not needed), so we only pass the first one.
        sdl2_mixer_recipe = self.get_recipe('sdl2_mixer', self.ctx)
        env["SDL2_MIXER_INCLUDE_DIR"] = sdl2_mixer_recipe.get_include_dirs(arch)[0]

        # NDKPLATFORM and LIBLINK are our switches for detecting Android platform, so can't be empty
        # FIXME: We may want to introduce a cleaner approach to this?
        env['NDKPLATFORM'] = "NOTNONE"
        env['LIBLINK'] = 'NOTNONE'

        # ffmpeg recipe enables GPL components only if ffpyplayer_codecs recipe used.
        # Therefor we need to disable libpostproc if skipped.
        if 'ffpyplayer_codecs' not in self.ctx.recipe_build_order:
            env["CONFIG_POSTPROC"] = '0'

        return env


recipe = FFPyPlayerRecipe()
