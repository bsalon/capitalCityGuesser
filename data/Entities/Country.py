class Country:
    def __init__(self, country_id, name, continent, capital_city):
        self.country_id = country_id
        self.name = name
        self.continent = continent
        self.capital_city = capital_city


    def __str__(self):
        return f"{self.name} in {self.continent} with capital {self.capital_city}"
