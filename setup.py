try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(name='tribone',
      version='0.0.0',
      provides=['tribone'],
      author='Andrew Tribone',
      author_email='atribone@gmail.com',
      url='tribone.us',
      packages=['tribone', 'tribone.lib', 'tribone.web'])
