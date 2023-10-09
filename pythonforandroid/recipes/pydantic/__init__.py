from pythonforandroid.recipe import PythonRecipe


class PydanticRecipe(PythonRecipe):
    version = '2.4.2'
    url = 'https://github.com/pydantic/pydantic/archive/refs/tags/v{version}.zip'
    depends = ['setuptools']
    python_depends = ['Cython', 'devtools', 'email-validator', 'typing-extensions', 'python-dotenv']
    call_hostpython_via_targetpython = False


recipe = PydanticRecipe()
