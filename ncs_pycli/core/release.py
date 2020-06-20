name = 'ncs_pycli'

_version_major = 1
_version_minor = 2
_version_patch = 1
_version_extra = None

# Construct full version string from these.
_ver = [_version_major, _version_minor, _version_patch]

__version__ = '.'.join(map(str, _ver))
if _version_extra:
    __version__ = __version__  + _version_extra

version = __version__  # backwards compatibility name
version_info = (_version_major, _version_minor, _version_patch, _version_extra)

description = "Gives you an interactive NSO python shell with tab completion."

license = 'MIT License'

authors = {
    'Hakan'    : ('Hakan Niska','hniska@cisco.com'),
    'Kiran'    : ('Kiran Kotari','kkotari@cisco.com'),
    }

author = ', '.join([each[0] for each in authors.values()])

author_email = ', '.join([each[1] for each in authors.values()])

url = 'https://github.com/NSO-developer/ncs_pycli.git'

platforms = [
    'OS Independent'
    ]

keywords = [
    'ncs-pycli', 
    'ncs_pycli', 
    'ncs interactive terminal', 
    'ncs ipython'
    ]

dev_status = {
    3: '3 - Alpha',
    4: '4 - Beta',
    5: '5 - Production/Stable',
    6: '6 - Mature'
    }

python_versions = [
    '2.7', 
    '3.5', 
    '3.6', 
    '3.7'
    ]

python_support = [
    'Programming Language :: Python :: {}'.format(each) \
        for each in python_versions
    ]

platform_support = [
    'Operating System :: {}'.format(each) \
        for each in platforms
]
classifiers = [
    'Framework :: IPython',
    'Intended Audience :: Developers',
    'Topic :: System :: Shells',
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: {}'.format(license),
    'Development Status :: {}'.format(dev_status[4]),
    ] 

classifiers += python_support 
classifiers += platform_support

trigger = [
    '{0}={0}.{0}:run'.format(name)
    ]

entry = True
entry_point = {
    'console_scripts': trigger
}