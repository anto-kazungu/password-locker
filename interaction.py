import sys
import random
import string
from app import Credentials  # Import Credentials class from app.py

class Menu:
    '''Class for the Menu items'''

    def __init__(self):
        self.accountdata = Credentials()  # Initialize Credentials instance
        self.choices = {
            "1": self.show_accounts,
            "2": self.add_account,
            "3": self.search_account,
            "4": self.delete_account,
            "5": self.password_generator,
            "6": self.quit
        }

    def display_menu(self):
        '''Display the menu items'''
        print("""
            Menu  
            1. Show accounts
            2. Add accounts
            3. Search account
            4. Delete account
            5. Generate password
            6. Quit
        """)

    def run(self):
        '''Display menu and respond to user choices'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_accounts(self, accounts=None):
        '''Display all accounts'''
        if not accounts:
            accounts = self.accountdata.accounts
        for account in accounts:
            print(account.account, account.username, account.password)

    def add_account(self):
        '''Add a new account'''
        account = input("Enter an account: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        self.accountdata.new_account(account, username, password)
        print("Your account has been added")

    def search_account(self):
        '''Search for an account using a filter'''
        filter_term = input("Search for: ")
        matching_accounts = self.accountdata.search_account(filter_term)
        self.show_accounts(matching_accounts)

    def delete_account(self, accounts):
        '''Delete a specified account'''
        print("Enter the account you want to delete")
        name = input()
        accounts.remove(name)
        print(f'Successfully removed {name}')

    def password_generator(self, length):
        '''Generate a password for an account'''
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(all_chars, length))
        return password


    def quit(self):
        '''Quit the program'''
        print("Goodbye")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
