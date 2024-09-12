import requests

class Currencies:
    def get_currency_list(self):
        self.url = "https://api.exchangerate-api.com/v4/latest/USD" 
        self.response = requests.get(self.url)
        self.data = self.response.json()

        return self.data['rates'].keys()

    def get_country_names(self, currencies):
        self.url = "https://restcountries.com/v3.1/all"
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.country_names = {}

        for currency in currencies:
            for country in self.data:
                if 'currencies' in country and currency in country['currencies']:
                    self.country_names[currency] = country['name']['common']
                    
        return self.country_names

    def display_currencies(self):
        self.currencies = self.get_currency_list()
        self.country_names = self.get_country_names(self.currencies)

        print("Available currencies:")
        print('-'*45)
        for currency, country in self.country_names.items():
            print(f"{currency}: {country}")
        print('-'*45)

