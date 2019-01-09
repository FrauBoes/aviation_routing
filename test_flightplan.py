from flightplan import Flightplan


def test_flightplan():
    x = Flightplan(('DUB','LHR','SYD','JFK','AAL','777'))

    x.enqueue('DUB')
    x.enqueue('AAL')
    x.enqueue('JFK')
    x.enqueue('SYD')
    x.enqueue('LHR')

    x.setAircraft('777')

    print(x.getAllRoutes())

    print(x.getFlightplan())

    print(x.getAircraft())

    print(x)

test_flightplan()
