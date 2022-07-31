from setuptools import find_packages
from setuptools import setup


setup(
    name='TuiTyping',
    version='0.0.1',
    license='MIT',
    url='https://github.com/jakubiee/TuiTyping',
    packages=find_packages(),
    package_data={'src':['languages/*.json']},
    include_package_data = True,
    entry_points={
        'console_scripts':[
            'tt = src.main:main', 
        ],
    },
)
    

