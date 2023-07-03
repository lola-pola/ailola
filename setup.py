from setuptools import setup, find_packages
import random
import os

build_number = os.environ.get("build_number", str(random.randint(0, 9999)) )
setup(
    name='ailola',
    version=f'0.9.{build_number}',
    license='MIT',
    author="Elhay Efrat",
    author_email='elhayefrat@gmail.com',
    package_dir = {'': 'ailola'},
    url='https://github.com/lola-pola/ailola',
    keywords='lola cli terraform ai',
    install_requires=['click', 'requests' ,'openai','colorama'],
    entry_points={'console_scripts': ['ailola = ailola:cli']}

)