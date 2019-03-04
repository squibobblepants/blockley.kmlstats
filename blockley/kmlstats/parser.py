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
from blockley.kmlstats.models.kml import SkitudeKML
from blockley.kmlstats.models.stats import Stats, DataPoints

class KMLParser:
    def __init__(self):
        self.stats = None
        self.datapoints = DataPoints()

    def parseSkitudeKML(self, kmlfilepointer):
        """Expects a file pointer from which it should be able to parse some KML"""
        kml_file = SkitudeKML(kmlfilepointer)
        # Just to stop the linter complaining
        return kml_file

if __name__ == "__main__":
    print("This is really only here for testing purposes, please remove it once we're eggable")
    x = KMLParser()
    fp = open("kml/2019-03-01 final run.kml", "r")
    x.parseSkitudeKML(fp)
    