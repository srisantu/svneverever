#!/usr/bin/env python
# Copyright (C) 2010 Sebastian Pipping <sebastian@pipping.org>
# Licensed under GPL v3 or later

from distutils.core import setup

import sys
sys.path.insert(0, 'modules')
from svneverever.version import VERSION_STR

setup(
    name='svneverever',
    description='Tool collecting path entries across SVN history',
    license='GPL v3 or later',
    version=VERSION_STR,
    url='https://github.com/hartwork/svneverever',
    download_url='https://github.com/hartwork/svneverever/archive/v%s.tar.gz' % VERSION_STR,
    author='Sebastian Pipping',
    author_email='sebastian@pipping.org',
    package_dir={'':'modules', },
    packages=['svneverever', ],
    scripts=['svneverever', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities',
    ],
)
