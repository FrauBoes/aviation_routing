import csv
from aircraft import Aircraft


class AircraftList:
    """
    Class to store aircrafts in dictionary with variety of lookup options
    """
    def __init__(self, csvfile):
        self.aircraftlist = self.loadData(csvfile)

    def loadData(self, csvfile):
        """
        :param csvFile
        :return: dictionary with aircrafts. Keys: airport code
        """
        list = {}

        try:  # Try to read file
            with open(csvfile, "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    if line[0] in list:
                        continue
                    else:
                        try:
                            # Unit conversion from miles to km if required
                            range = float(line[4])

                            if line[2] == 'imperial':
                                range *= 1.609344

                            elif line[2] != 'metric':
                                print('Unit not specified in line' + str(line) + '. Saved as kilometers.')

                            list[line[0]] = Aircraft(line[3], line[0], line[1], range)

                        except ValueError:
                            continue
            return list

        except FileNotFoundError:  # If file not found print message
            print('File ' + str(csvfile) + ' not found.')

    # Get aircraft object
    def getAircraft(self, code):
        return self.aircraftlist[code]


