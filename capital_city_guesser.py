#!/usr/bin/env python3.7

import zeep

class GuesserApp:
    def __init__(self):
        self.client = zeep.Client("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")

    def run(self):
        pass


def main():
    guesser_app = GuesserApp()
    guesser_app.run()

if __name__ == "__main__":
    main()
