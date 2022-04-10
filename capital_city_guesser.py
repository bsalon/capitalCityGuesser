import zeep


class GuesserApp:
    def __init__(self):
        self.client = zeep.Client("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")
        self.__initialize_continents_dict()


    def __initialize_continents_dict(self):
        continents = self.__get_countries_by_continent()
        continents_with_capitals = self.__add_capitals_to_continent_countries(continents)
        continents_dict = self.__create_continent_countries_dict(continents_with_capitals)
        self.continents = continents_dict


    def __get_countries_by_continent(self):
        all_continents = self.client.service.ListOfCountryNamesGroupedByContinent()
        return filter(lambda c: "Antarctica" not in c["Continent"]["sName"], all_continents)


    def __create_continent_countries_dict(self, continents_with_capitals):
        continents_dict = {}
        for continent in continents_with_capitals:
            continent_name = continent['Continent']['sName'].strip()
            continents_dict[continent_name] = []

            for country in continent['CountryCodeAndNames']['tCountryCodeAndName']:
                country_name = country['sName']
                country_capital = country['sCapitalCity']
                continents_dict[continent_name].append((country_name, country_capital))

        return continents_dict


    def __add_capitals_to_continent_countries(self, continents):
        return map(lambda c : self.__add_capitals_to_continent(c), continents)


    def __add_capitals_to_continent(self, c):
        for i in range(len(c['CountryCodeAndNames']['tCountryCodeAndName'])):
            country = c['CountryCodeAndNames']['tCountryCodeAndName'][i]
            country_ISOCode = country['sISOCode']
            country['sCapitalCity'] = self.client.service.CapitalCity(country_ISOCode)
        return c
