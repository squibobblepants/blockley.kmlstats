#    blockley.kmlstats is a reusable python library for generating various statistics from a given KML File
#    or list of KML files
#
#    Copyright © 2019 Tom Blockley
#
#    This file is part of blockley.kmlstats.
#
#    blockley.kmlstats is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    blockley.kmlstats is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with blockley.kmlstats. If not, see <http://gnu.org/licenses/>.
from distutils.core import setup

setup(
    name='blockley.kmlstats',
    version='0.0.1dev',
    packages=['blockley.kmlstats',],
    license='GNU LESSER GENERAL PUBLIC LICENSE Version 3',
    long_description=open('README.md').read(),
    install_requires=[
        'beautifulsoup4==4.7.1',
        'lxml==3.7.2',
        'GeoPy==1.18.1'
    ]
)