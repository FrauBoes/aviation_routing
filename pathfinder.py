

def pathfinder(flightplan, aircraftlist, airportatlas):
    """
    Find the best route and its cost for an input of a number of airports and a given aircraft

    Return the first one found if there are multiple best routes
    :param flightplan: object with list of five airports
    :param aircraftlist: dictionary of aircrafts
    :param airportatlas: dictionary of airports
    :return: tuple of airports that makes the best route, float cost
    """

    all_routes = flightplan.getAllRoutes()  # Get all possible permutation of flightplan
    flightrange = aircraftlist.getAircraft(flightplan.getAircraft()).getFlightrange()  # Get flightrange of aircraft

    best_flightplan = None
    best_sum = None

    for i in all_routes:
        sum = 0
        in_range = True

        for j in range(len(i)-1):
            # Get codes of current pair of airports
            a1 = airportatlas.getAirport(i[j]).getCode()
            a2 = airportatlas.getAirport(i[j+1]).getCode()

            distance = airportatlas.getDistanceBetweenAirports(a1, a2)

            # If flightrange < distance to travel, ignore current permutation
            if flightrange < distance:
                in_range = False
                break

            cost = airportatlas.getCostBetweenAirports(a1, a2)
            sum += cost

        # Store current best flightplan and cost
        if in_range and (best_sum is None or sum < best_sum):
            best_sum = sum
            best_flightplan = i

    if best_flightplan is None:
        return best_flightplan, None

    else:
        return best_flightplan, round(best_sum,2)





