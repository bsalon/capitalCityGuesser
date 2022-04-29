#!/usr/bin/env python3.7

from data.CountryClient import CountryClient
from data.Services.CountryService import CountryService

def main():
    country_client = CountryClient("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")
    countries = country_client.countries

    country_service = CountryService()
    if not country_service.has_at_least_rows(100):
        country_service.clear_table()
        country_service.insert_countries(list(countries))

    for country in country_service.get_all_countries():
        print(country)


if __name__ == "__main__":
    main()
