from cx_Freeze import setup, Executable

setup(name = 'urlParse',
      version = '0.01',
      description = 'Parse stuff',
      executables = [Executable("szamol.py")])
