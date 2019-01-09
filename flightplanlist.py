import csv
from flightplan import Flightplan


class FlightplanList:
    """
    Class to store flightplans in dictionary with variety of lookup options

    Key: flightplan string
    """
    def __init__(self, csvfile, airportatlas, aircraftlist):
        self.flightplan_list = self.loadFlightplans(csvfile, airportatlas, aircraftlist)

    def loadFlightplans(self, csvfile, airportatlas, aircraftlist):
        """
        Load data required to invoke flightplan objects

        :param csv_input: csv file with itineraries, airportatlas and aircraftlist
        :return: dictionary of itinerary objects
        """
        flightplan_list = {}

        # Read file with list of flightplans
        try:
            with open(csvfile, "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:

                    f = Flightplan(" ".join(line))

                    # Add airport if found as stored airport object
                    try:
                        for item in line[:-1]:
                            airportatlas.getAirport(item)
                            f.enqueue(item)

                    # Otherwise ignore flightplan
                    except KeyError:
                        print('An airport in line ' + str(line) + ' could not be found, itinerary in this line ignored.')
                        continue

                    # Add aircraft if found as stored aircraft object
                    try:
                        aircraftlist.getAircraft(line[-1])
                        f.setAircraft(line[-1])

                    # Otherwise ignore flightplan
                    except KeyError:
                        print('Aircraft in line ' + str(line) + ' could not be found, itinerary in this line ignored.')
                        continue

                    flightplan_list[" ".join(line)] = f

            return flightplan_list

        except FileNotFoundError:
            print('File ' + csvfile + ' not found.')

    # Get flightplan object
    def getFlightplan(self, flightplan):
        return self.flightplan_list[flightplan]

