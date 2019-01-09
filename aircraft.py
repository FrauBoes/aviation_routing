class Aircraft:
    """Class to store aircraft objects"""

    def __init__(self, make, code, typ, flightrange):
        self.make = make
        self.code = code
        self.typ = typ
        self.flightrange = float(flightrange)  # Unit kilometers

    def getMake(self):
        return self.make

    def getCode(self):
        return self.code

    def getTyp(self):
        return self.typ

    def getFlightrange(self):
        return self.flightrange

    def __str__(self):
        return str(self.getMake()) + " " + str(self.getCode()) + " " + str(self.getTyp()) + str(self.getFlightrange())
