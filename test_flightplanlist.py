from aircraftlist import AircraftList
from airportatlas import AirportAtlas
from flightplanlist import FlightplanList
from directory import *


def test_flightplanlist():
    # Load all required data
    aircraftlist = AircraftList(file_aircraft)

    airportatlas = AirportAtlas(file_airports, file_currencyrates, file_countrycurrency)
    flightplans = FlightplanList(test_file_input, airportatlas, aircraftlist)

    for i in flightplans.flightplan_list:
        print(i)
        print(flightplans.flightplan_list[i])
        print(flightplans.flightplan_list[i].getFlightplan())
        print(flightplans.flightplan_list[i].getAircraft())
        print(flightplans.flightplan_list[i].getAllRoutes())
        print(flightplans.flightplan_list[i].size())

test_flightplanlist()