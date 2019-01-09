import csv
from pathfinder import pathfinder


def writeOutput(output, flightplanlist, aircraftlist, airportatlas):
    # Write ro file
    try:
        with open((output), 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, escapechar='-', quoting=csv.QUOTE_NONE, delimiter='|')
            spamwriter.writerow(['flightplan - cheapest_route - fuel_cost'])

            for x in flightplanlist.flightplan_list:

                # Save best_route and best_cost for flightplan x as its data fields
                y, z = pathfinder(flightplanlist.flightplan_list[x], aircraftlist, airportatlas)

                flightplanlist.flightplan_list[x].setBestRoute(y)
                flightplanlist.flightplan_list[x].setBestCost(z)

                # Write line to file with flightplan, its best route and cost
                spamwriter.writerow(
                    [flightplanlist.flightplan_list[x].getFlightplan() + ' - ' + str(y) + ' - ' + str(z)])

        print('Output written to file: ' + output + '.')

    except FileNotFoundError:
        print('File ' + output + ' not found.')
