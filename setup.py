from setuptools import setup, find_packages

common_requires = [ 'rcli >= 0.4.0, < 0.5' ]
setup(install_requires=[] + common_requires,
      setup_requires=[] + common_requires,
      autodetect_commands=True,
      packages=find_packages())
