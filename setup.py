from distutils.core import setup

setup(
    name='Libdw',
    version='2.0.0',
    author='Oka Kurniawan',
    author_email='oka_kurniawan@sutd.edu.sg',
    packages=['amigobot','libdw','soar2','soar2.io','soar2.outputs','soar2.serial','soar2.controls','soar2.graphics','soar2.worlds','form','examples'],
    url='',
    license='LICENSE.txt',
    description='Package for Digital World.',
    long_description=open('README.txt').read(),
)
