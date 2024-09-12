import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Option:
    def display_options(self):
        while True:
            choice = input(f"{'-'*45}\n"
                            "1: Get the exchange rate of two currencies\n"
                           "2: Convert from one currency to another \n"
                           f"{'-'*45}\n")
            if choice not in ['1' , '2']:
                print("Your input is incorrect try again")
            else:
                break

        return choice
    

    def continue_options(self):
        while True:
            continue_choice = input(f"{'-'*45}\n"
                            "1: Do you want to continue\n"
                           "2: Quit \n"
                           f"{'-'*45}\n")
            if continue_choice not in ['1' , '2']:
                print("Your input is incorrect try again")
            else:
                clear_screen()
                break
            
        return continue_choice