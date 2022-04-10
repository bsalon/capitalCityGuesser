#!/usr/bin/env python3.7

from CountryClient import CountryClient

def main():
    country_client = CountryClient("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")
    print(country_client.continents)

if __name__ == "__main__":
    main()
