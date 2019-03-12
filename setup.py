"""A Docker based CLI Tools manager.

See: https://github.com/kkarolis/ctshed
"""

from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ctshed',
    description='A Docker based CLI Tools manager.',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
        'mock',
        'coveralls',
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
            'ctshed=ctshed.cli:main'
        ]
    },
    url='https://github.com/kkarolis/ctshed',
)
