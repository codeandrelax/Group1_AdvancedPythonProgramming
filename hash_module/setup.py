from setuptools import setup, Extension

hash_module = Extension('hash_module', sources=['hash.c'])

setup(
    name='hash_module',
    version='1.0',
    description='Python module for hashing passwords',
    author='Group1 Advanced Python',
    ext_modules=[Extension('hash_module', sources=['hash.c'])],
)
