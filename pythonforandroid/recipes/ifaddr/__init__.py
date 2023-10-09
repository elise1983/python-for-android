from pythonforandroid.recipe import PythonRecipe


class IfaddrRecipe(PythonRecipe):
    name = 'ifaddr'
    version = '0.2.0'
    url = 'https://pypi.python.org/packages/source/i/ifaddr/ifaddr-{version}.tar.gz'
    depends = ['setuptools', 'ifaddrs', 'ipaddress']
    call_hostpython_via_targetpython = False
    patches = ["getifaddrs.patch"]


recipe = IfaddrRecipe()
