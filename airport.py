class Airport:
    """Class to store airport objects"""

    def __init__(self, code, country, lat, long, rate):
        self.code = code
        self.country = country
        self.lat = float(lat)
        self.long = float(long)
        self.rate = float(rate)  # To-Euro-rate of country where airport is located

    def getCode(self):
        return self.code

    def getCountry(self):
        return self.country

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def getRate(self):
        return self.rate

    def __str__(self):
        return "Code: " + str(self.getCode()) + " Country: " + str(self.getCountry()) + " Lat: " + str(self.getLat()) \
               + " Long: " + str(self.getLong()) + " Rate: " + str(self.getRate())
