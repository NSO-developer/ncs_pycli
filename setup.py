from os import path
from io import open
from setuptools import setup, find_packages
from ncs_pycli.core import release as rel


here = path.abspath(path.dirname(__file__))
reqs = []

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    read_lines = f.readlines()
    reqs = [each.strip() for each in read_lines]

setup(
    name           = rel.name,
    url            = rel.url,
    version        = rel.version,
    description    = rel.description,
    author         = rel.author,
    author_email   = rel.author_email,
    classifiers    = rel.classifiers,
    keywords       = rel.keywords,
    entry_point    = rel.entry_point if rel.entry else {},

    install_requires = reqs,
    long_description = long_description,
    packages         = find_packages(where='.', exclude=['tests']),

    include_package_data          = True,
    long_description_content_type = 'text/markdown',
)

