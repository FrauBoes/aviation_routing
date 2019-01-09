from itertools import permutations


class Flightplan:
    """
    Class to store flightplan objects. A Flightplan class defines a container object for a flightplan.

    Implements flightplan object as a queue using a list
    Provides methods to access the first and last item in the flightplan
    Store aircraft as data field of a flightplan object to get range
    """
    def __init__(self, flightplan):
        self.flightplan = str(flightplan)
        self.items = []
        self.aircraft = None
        self.best_route = None
        self.best_cost = None

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def getFlightplan(self):
        return self.flightplan

    def setAircraft(self, aircraft):
        self.aircraft = aircraft

    def getAircraft(self):
        return self.aircraft

    def setBestRoute(self, best_route):
        self.best_route = best_route

    def getBestRoute(self):
        return self.getBestRoute

    def setBestCost(self, best_cost):
        self.best_cost = best_cost

    def getBestCost(self):
        return self.getBestCost

    def getAllRoutes(self):
        """
        :return: Successive permutations of all airports of all airports other than start/end

        Start/end airport is added at the start and end of each permutation
        """
        start_airport = self.dequeue()
        all_routes = []

        for route in permutations(self.items):
            all_routes.append((start_airport, ) + route + (start_airport, ))

        return all_routes

    def __str__(self):
        return self.getFlightplan()