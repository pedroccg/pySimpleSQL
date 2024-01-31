from setuptools import setup, find_packages

setup(
    name='pySimpleSQL',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'mysql-connector-python',
        'IPython'
    ],
    author='Pedro Guimaraes',
    author_email='pedro.guimaraes@dsi.uminho.pt',
    description='A simple library for running SQL queries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xskid/pySimpleSQL',
    license='MIT'
)