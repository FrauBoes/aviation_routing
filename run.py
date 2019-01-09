# Main script running the application

from aircraftlist import AircraftList
from airportatlas import AirportAtlas
from flightplanlist import FlightplanList
from utils import writeOutput
from directory import *

# Ask user to confirm required files
files_confirmed = input("Hello! \n"
                        "Before you can search the best route of a flightplan, \n"
                        "please confirm that the search is based on the following files: \n\n"
                        + str(file_aircraft) + ' \n'
                        + str(file_airports) + ' \n'
                        + str(file_currencyrates) + ' \n'
                        + str(file_countrycurrency + '\n\n'
                              "Please type 'c' to confirm or 'e' to stop the program: "))

# Stop if files not confirmed
if files_confirmed == 'e':
    print("Program stopped. Please update files before restarting.")

# Otherwise proceed and load required files
elif files_confirmed == 'c':
    print('Program continuing. Reading files...')

    print('Log ' + file_aircraft + ': ')
    aircraftlist = AircraftList(file_aircraft)

    try:
        print('Log airportatlas: ')
        airportatlas = AirportAtlas(file_airports, file_currencyrates, file_countrycurrency)

        try:
            # Ask user for input and ouput csv
            file_flightplan = input("Please type in the name of the input file (example: flightplans.csv): ")
            output = input("Please type in the name of the output file (example: output.csv): ")

            # Create flightplans based on input file
            flightplanlist = FlightplanList(file_flightplan, airportatlas, aircraftlist)

            try:
                # Write output to file
                writeOutput(output, flightplanlist, aircraftlist, airportatlas)

            except TypeError:
                print('Output could not be written to file.')

        except TypeError:
            print(file_flightplan + 'could not be read.')

    except TypeError:
        print('Airportatlas could not be created.')

# Stop program if input unexpected
else:
    print("Program stopped due to unexpected input.")
