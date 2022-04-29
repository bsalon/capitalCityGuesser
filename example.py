#!/usr/bin/env python3.7

from data.CountryClient import CountryClient
from data.Services.CountryService import CountryService

def main():
    country_client = CountryClient("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")
    country_service = CountryService()
    print(list(country_client.countries))

if __name__ == "__main__":
    main()
