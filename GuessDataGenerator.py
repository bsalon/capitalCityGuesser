#!/usr/bin/env python3.7

from data.CountryClient import CountryClient

from datetime import datetime
import random


class GuessDataGenerator:
    def __init__(self, country_service):
        self.country_service = country_service

    def generate_guess_data(self, guesses, countries):
        country_map = [(country, False) for country in self.country_service.get_all_countries()]

        random.seed(datetime.now())
        guess_data = []
        for i in range(guesses):
            guess_capital = []

            while len(guess_capital) < countries:
                country_index = random.randint(0, len(country_map) - 1)
                if country_map[country_index][1]:
                    continue
                guess_capital.append(country_map[country_index][0])
                country_map[country_index] = (country_map[country_index][0], True)

            correct = random.randint(0, len(guess_capital) - 1)
            guess_data.append((guess_capital, correct))

        return guess_data
