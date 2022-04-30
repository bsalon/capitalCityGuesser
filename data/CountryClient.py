import zeep


class CountryClient(zeep.Client):
    def __init__(self, *args, **kwargs):
        super(CountryClient, self).__init__(*args, **kwargs)
        self.__initialize_countries()


    def __initialize_countries(self):
        continents = self.__get_countries_by_continent()
        continents_with_capitals = self.__add_capitals_to_continent_countries(continents)
        countries_generator = self.__create_countries(continents_with_capitals)
        self.countries = countries_generator


    def __get_countries_by_continent(self):
        all_continents = self.service.ListOfCountryNamesGroupedByContinent()
        return filter(lambda c: "Antarctica" not in c["Continent"]["sName"], all_continents)


    def __create_countries(self, continents_with_capitals):
        for continent in continents_with_capitals:
            continent_name = continent['Continent']['sName'].strip()

            for country in continent['CountryCodeAndNames']['tCountryCodeAndName']:
                country_name = country['sName']
                country_capital = country['sCapitalCity']
                yield (country_name, continent_name, country_capital)


    def __add_capitals_to_continent_countries(self, continents):
        return map(lambda c : self.__add_capitals_to_continent(c), continents)


    def __add_capitals_to_continent(self, c):
        for i in range(len(c['CountryCodeAndNames']['tCountryCodeAndName'])):
            country = c['CountryCodeAndNames']['tCountryCodeAndName'][i]
            country_ISOCode = country['sISOCode']
            country['sCapitalCity'] = self.service.CapitalCity(country_ISOCode)
        return c
