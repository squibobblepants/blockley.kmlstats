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
from geopy.distance import distance
class Stats:
    def __init__(self, datapoints):
        # Initialise our instance variables
        self.distance    = 0
        self.ascent      = 0
        self.descent     = 0
        self.time        = 0
        self.moving_time = 0
        self.speed_asc   = 0
        self.speed_desc  = 0

        # Process the datapoints we were passed
        self.updateStats(datapoints)
    
    def updateStats(self, datapoints):
        print("TODO: Calculate Stats")

    def __repr__(self):
        return (
            "Distance:         {distance:d}km\n"
            "Ascent:           {ascent:d}km\n"
            "Descent:          {descent:d}km\n"
            "Time:             {time:d}m\n"
            "Moving Time:      {moving_time:d}m\n"
            "Top Speed (Asc):  {speed_asc:d}km/h\n"
            "Top Speed (Desc): {speed_asc:d}km/h\n"
        ).format(
            distance = self.distance,
            ascent = self.ascent,
            descent = self.descent,
            time = self.time,
            moving_time = self.moving_time,
            speed_asc = self.speed_asc,
            speed_desc = self.speed_desc
        )

# Some static variables mostly just used by the DataPoints class
UP   = "UP"
DOWN = "DOWN"

class DataPoints:
    def __init__(self):
        # Initialise a tonne of instance variables ready for use
        self.speeds = {
            'ascending':  [],
            'descending': []
        }
        self.distances = {
            'total':      [],
            'ascending':  [],
            'descending': []
        }
        self.times = {
            'total':  [],
            'moving': []
        }
        self.last_data_point = None
        self.direction = UP
    
    def processPoint(self, datapoint):
        print("TODO: Process Data Point")
