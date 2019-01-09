import pytest
from airportatlas import AirportAtlas
from directory import *


def test_atlas():
    x = AirportAtlas(file_airports, file_currencyrates, file_countrycurrency)

    assert x.airportatlas is not None
    assert x.getAirport('ZAD') is not None

    a1 = x.getAirport('DJO')
    a2 = x.getAirport('OSI')

    assert a2.getCountry() == "Croatia"
    assert a1.getCode() == 'DJO'

    print(a2.getRate())
    print(x.getDistanceBetweenAirports('SNN', 'ORK'))
    print(x.getDistanceBetweenAirports('ORK', 'CDG'))
    print(x.getDistanceBetweenAirports('CDG', 'SIN'))
    print(x.getDistanceBetweenAirports('SIN', 'MAN'))
    print(x.getDistanceBetweenAirports('MAN', 'SNN'))

    for c in x.airportatlas:
        print(x.getAirport(c))

    assert x.getCostBetweenAirports('DJO', 'OSI') is not None

    print(x.getCostBetweenAirports('SNN', 'ORK'))
    print(x.getCostBetweenAirports('ORK', 'CDG'))
    print(x.getCostBetweenAirports('CDG', 'SIN'))
    print(x.getCostBetweenAirports('SIN', 'MAN'))
    print(x.getCostBetweenAirports('MAN', 'SNN'))

test_atlas()