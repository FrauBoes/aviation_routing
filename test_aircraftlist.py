import pytest
from aircraftlist import AircraftList
from directory import *


def test_aircraftlist():
    x = AircraftList(file_aircraft)

    assert x.aircraftlist is not None
    assert x.getAircraft('767') is not None

    a1 = x.getAircraft('767')

    print(a1.getCode())
    print(a1.getMake())
    print(a1.getTyp())
    print(a1.getFlightrange())

    for a in x.aircraftlist:
        print(x.getAircraft(a))

test_aircraftlist()