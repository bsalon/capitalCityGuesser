#!/usr/bin/env python3.7

import zeep

class GuesserApp:
    def __init__(self):
        self.client = zeep.Client("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")
        self.continents = list(self.get_countries_by_continent())

    def get_countries_by_continent(self):
        all_continents = self.client.service.ListOfCountryNamesGroupedByContinent()
        return filter(lambda x: "Antarctica" not in x["Continent"]["sName"], all_continents)

    def run(self):
        pass


def main():
    guesser_app = GuesserApp()
    guesser_app.run()

if __name__ == "__main__":
    main()
