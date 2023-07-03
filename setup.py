from setuptools import setup, find_packages


setup(
    name='ailola',
    version='0.9.0',
    license='MIT',
    author="Elhay Efrat",
    author_email='elhayefrat@gmail.com',
    package_dir = {'': 'ailola'},
    url='https://github.com/lola-pola/ailola',
    keywords='lola cli terraform ai',
    install_requires=['click', 'requests' ,'openai','colorama'],
    entry_points={'console_scripts': ['ailola = ailola:cli']}

)