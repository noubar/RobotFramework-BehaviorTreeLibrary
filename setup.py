from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from src.BehaviorTreeLibrary.version import VERSION

CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3 :: Only
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()
with open(join(CURDIR, 'README.md')) as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name             = 'robotframework-BehaviorTreeLibrary',
    version          = VERSION,
    description      = 'Behavior Tree library for Robot Framework',
    # long_description = DESCRIPTION,
    long_description_content_type="text/markdown",
    author           = 'noubar',
    url              = 'https://github.com/noubar/BehaviorTreeLibrary',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework testing testautomation behaviourtree',
    platforms        = 'any',
    classifiers      = CLASSIFIERS,
    python_requires  = '>=3.6, <4',
    install_requires = REQUIREMENTS,
    package_dir      = {'BehaviorTreeLibrary': 'src/BehaviorTreeLibrary'},
    packages         = find_packages('src'),
    package_data     ={'BehaviorTreeLibrary': ['*.pyi']}
)
