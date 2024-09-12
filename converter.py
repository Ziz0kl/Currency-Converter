from option import Option
from currencies import Currencies
import requests

import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Converter:
    def __init__(self):
        self.option = Option()
        self.currencies = Currencies()


    def start(self):
        while True:
            choice = self.option.display_options()
            clear_screen()

            if choice == '1':
                self.exchange_rate()

            else:
                self.convert()

            if self.option.continue_options() == '2':
                clear_screen()
                print("Thanks for visiting us!")
                break 
                                


    def exchanged_currencies(self):
        while True:
            self.from_currency = input("Please enter your currency: ").upper()
            if self.from_currency in self.currencies.currencies:
                break
            else:
                print("Your input is incorrect try again")
        while True:
            self.to_currency = input("Please enter the currency to convert to: ").upper()
            if self.to_currency in self.currencies.currencies:
                break
            else:
                print("Your input is incorrect try again")
        


    def exchange_rate(self):
        self.currencies.display_currencies()
        self.exchanged_currencies()
        url = f"https://api.exchangerate-api.com/v4/latest/{self.from_currency}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'].get(self.to_currency)
            
        print(f"Exchange rate from {self.from_currency} to {self.to_currency} is {rate}")
        
        return rate


    def convert(self):
        rate = self.exchange_rate()
        amount = float(input(f"Please enter the amount in {self.from_currency}: "))
        converted_amount = amount * rate

        print(f"{amount} {self.from_currency} is equal to {converted_amount:.2f} {self.to_currency}")
            

start = Converter()
start.start()
