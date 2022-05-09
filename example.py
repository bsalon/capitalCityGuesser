#!/usr/bin/env python3.7

from data.CountryClient import CountryClient
from data.Services.CountryService import CountryService

from GUIManager import GUIManager


def main():
    print("Starting the application")
    print("Getting the data from the client")
    country_client = CountryClient("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")
    countries = list(country_client.countries)

    in_memory = False
    if not in_memory:
        country_service = CountryService()
        if not country_service.has_at_least_rows(100):
            country_service.clear_table()
            country_service.insert_countries(list(countries))

    gui = GUIManager(countries if in_memory else None)
    gui.run()


if __name__ == "__main__":
    main()
