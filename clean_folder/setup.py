from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='this package sorts out files',
    url='https://github.com/Barskyi',
    author='Barskyi Taras',
    author_email='barskyi69@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean.py:search_path']}
)
