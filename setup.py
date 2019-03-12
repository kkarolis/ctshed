"""A Docker based CLI Tools manager.

See: https://github.com/kkarolis/cledocker
"""

from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# FIXME add mock,unittest to test requires
setup(
    name='cledocker',
    description='A Docker based CLI Tools manager.',
    long_description=long_description,
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
        'pytest-runner',
    ],
    install_requires=[
        'Click',
        'jinja2',
    ],
    tests_require=[
        'pytest',
        'mock'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'cledocker=cledocker.cli:main'
        ]
    },
    url='https://github.com/kkarolis/cledocker',
)
