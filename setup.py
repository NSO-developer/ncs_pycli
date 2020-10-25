from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
reqs = []

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, '.version'), encoding='utf-8') as f:
    version = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    read_lines = f.readlines()
    reqs = [each.strip() for each in read_lines]

setup(
    name = 'ncs_pycli',
    version = version,
    description = "Gives you an interactive NSO python shell with tab completion.",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/NSO-developer/ncs_pycli.git',
    author = 'Hakan Niska, Kiran Kumar Kotari',
    author_email = 'hniska@cisco.com, kkotari@cisco.com',
    entry_points={
        'console_scripts': [
            'ncs_pycli=ncs_pycli.ncs_pycli:run',
            'ncs-pycli=ncs_pycli.ncs_pycli:run',
        ],
    },
    install_requires=reqs,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    keywords = 'ncs-pycli ncs_pycli',
    packages = find_packages(where='.', exclude=['tests']),
    include_package_data=True,
)

