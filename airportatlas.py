import csv
from airport import Airport
from math import pi, sin, cos, acos


class AirportAtlas:
    """
    Class to store airports in dictionary with variety of lookup options
    """
    def __init__(self, csv_airport, csv_currencyrate, csv_countrycurrency):
        self.airportatlas = self.loadData(csv_airport, csv_currencyrate, csv_countrycurrency)

    def loadData(self, csv_airport, csv_currencyrate, csv_countrycurrency):
        """
        Load data from all files required for airport object

        :return: dictionary with airports. Keys: airport code
        """
        rates = {}

        # Read file with currency code and from-euro-rate mapping
        try:
            with open(csv_currencyrate, "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    if line[1] in rates:
                        continue
                    else:
                        rates[line[1]] = line[2]

        except FileNotFoundError:
            print('File ' + csv_currencyrate + ' not found.')

        countries = {}

        # Read file with country name and currency code mapping
        try:
            with open(csv_countrycurrency, "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    if line[0] in countries:
                        continue
                    else:
                        try:
                            countries[line[0]] = rates[line[14]]
                        except KeyError:
                            continue

        except FileNotFoundError:
            print('File ' + csv_countrycurrency + ' not found.')

        atlas = {}

        # Read file with airport information
        try:
            with open(csv_airport, "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    if line[4] in atlas:
                        continue
                    else:
                        try:
                            atlas[line[4]] = Airport(line[4], line[3], line[6], line[7], countries[line[3]])
                        except KeyError:
                            print(line[4] + ' airport has missing values, not added to airportatlas.')
            return atlas

        except FileNotFoundError:
            print('File ' + csv_airport + ' not found.')

    # Get airport object
    def getAirport(self, code):
        return self.airportatlas[code]

    @staticmethod
    def greatcircledist(lat1, long1, lat2, long2):
        """
        Calculate distance * 2 to given airport and return is as float
        """
        radius_earth = 6371    # km
        theta1 = long1 * (2 * pi) / 360
        theta2 = long2 * (2 * pi) / 360
        phi1 = (90 - lat1) * (2 * pi) / 360
        phi2 = (90 - lat2) * (2 * pi) / 360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth
        return distance

    def getDistanceBetweenAirports(self, code1, code2):
        """
        Take two airports and return the distance between them as float
        :param code1: airport 1
        :param code2: airport 2
        """
        a1 = self.getAirport(code1)
        a2 = self.getAirport(code2)
        return AirportAtlas.greatcircledist(a1.getLat(), a1.getLong(), a2.getLat(), a2.getLong())

    def getCostBetweenAirports(self, code1, code2):
        """
        Take two airports and return the cost of flight from airport 1 to airport 2
        Cost is from-euro-rate of airport 1 * distance
        :param code1: airport 1
        :param code2: airport 2
        """
        return self.getAirport(code1).getRate() * self.getDistanceBetweenAirports(code1, code2)


