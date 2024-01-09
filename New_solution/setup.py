from setuptools import setup, Extension, find_packages
 
hash_module = Extension('hash_module', sources=['usrmgm_library/hash.c'])
 
with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='usrmgmt_library',
    version='1.0',
    description='Python library for user management with password hashing',
    long_description=long_description,
    author='Group1 Advanced Python',
    packages=find_packages(),
    ext_modules=[hash_module],
)



# from setuptools import setup, Extension

# hash_module = Extension('hash_module', sources=['hash.c'])

# setup(
#     name='hash_module',
#     version='1.0',
#     description='Python module for hashing passwords',
#     author='Group1 Advanced Python',
#     ext_modules=[Extension('hash_module', sources=['hash.c'])],
# )
