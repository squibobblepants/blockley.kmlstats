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

from bs4 import BeautifulSoup
from datetime import datetime
from decimal import Decimal
from geopy.distance import distance, lonlat

class KMLPoint:
    """ Basic Representation of a KML point, currently only from what Skitude presents """
    def __init__(self):
        self.timestamp   = None
        self.geopoint    = None
        self.speed       = None
        # I'm really not sure that we care about inclination. It appears to be 1 or 0.
        self.inclination = None


class KMLFile:
    """ Basic extendable KMLFile representation, currently only extended to Skitude KML files """
    def __init__(self, filepointer):
        self.soup = BeautifulSoup(filepointer.read(), 'xml')
        self.timestamp = None
        self.points = []
        self.process()
    
    def process(self):
        """ This is the only function that should need overriding by different types of parser, I hope """
        raise NotImplementedError("Class %s doesn't implement process()" % (self.__class__.__name__))

class SkitudeKML(KMLFile):
    def __init__(self, filepointer):
        # Get the soup prepared and prepare a few other bits
        super().__init__(filepointer)
    
    def process(self):
        # Skitude KML files hold the Date information in the description field of the kml file 
        # for some reason. Why? Who knows? Also, it doesn't (I don't think) record in UTC, just
        # the local timezone, if you care about that kind of thing
        datestamp = self.soup.Document.find("name").string.strip()
        self.timestamp = datetime.strptime(datestamp, "%Y-%m-%d %H:%M:%S")
        
        # Next parse all the points
        for point in self.soup.Folder.find_all("Placemark"):
            kml_point = KMLPoint()
            kml_point.timestamp = datetime.fromtimestamp(int(point.TimeStamp.when.string))
            coords = point.Point.coordinates.string.split(",")
            kml_point.geopoint = lonlat(coords[0], coords[1], coords[2])
            self.points.append(kml_point)

            self.speed = Decimal(point.speed.string)
            self.inclination = Decimal(point.inclination.string)
        
        # Try things like distance(self.points[0].geopoint, self.points[1].geopoint).km and things.
        # See https://geopy.readthedocs.io/en/stable/#module-geopy.distance for info
        
        print("We now (should) have everything we require to process a route and determine the various things we care about")
