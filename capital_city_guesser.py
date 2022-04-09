#!/usr/bin/env python3.7


import zeep


class GuesserApp:
    def __init__(self):
        self.client = zeep.Client("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")
        self.__initialize_continents_dict()


    def __initialize_continents_dict(self):
        continents = self.__get_countries_by_continent()
        self.continents = list(self.__add_capitals_to_continent_countries(continents))


    def __get_countries_by_continent(self):
        all_continents = self.client.service.ListOfCountryNamesGroupedByContinent()
        return filter(lambda c: "Antarctica" not in c["Continent"]["sName"], all_continents)


    def __add_capitals_to_continent_countries(self, continents):
        return map(lambda c : self.__add_capitals_to_continent(c), continents)


    def __add_capitals_to_continent(self, c):
        for i in range(len(c['CountryCodeAndNames']['tCountryCodeAndName'])):
            country = c['CountryCodeAndNames']['tCountryCodeAndName'][i]
            country_ISOCode = country['sISOCode']
            country['sCapitalCity'] = self.client.service.CapitalCity(country_ISOCode)
        return c


    def run(self):
        pass



def main():
    guesser_app = GuesserApp()
    guesser_app.run()


if __name__ == "__main__":
    main()
