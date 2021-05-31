
from app import allacounts
class Menu:
     
 '''
 Class for the Menu items
 '''
 def __init__(self):
      self.accountdata = allacounts() #imported class from app module
 
      self.choices = {    #menu items that will be accessed 
 
           "1" : self.show_accounts,
           "2" : self.add_account,
           "3" : self.search_account,
           "4" : self.delete_account,
           "5" : self.password_generator,
           "6" : self.quit
        }

 def display_menu(self): #Display for the menu items
     
       print(""" 

             Notebook Menu  
 
             1. Show accounts
             2. Add accounts
             3. Search account
             4. Delete account
             5. Generate password
             6.Quit
 
             """)

 # For directing the user selection to the required task

 def run(self):
 
     ''' Display menu and respond to user choices '''
     while True:
 
           self.display_menu()
 
           choice = input("Enter an option: " )
 
           action = self.choices.get(choice)
 
           if action:
 
                action()
 
           else:
 
              print("{0} is not a valid choice".format(choice))

 # For displaying all the accounts in the array
 
 def show_accounts(self, accounts=None):
 
     ''' Display all diaries in diarybook '''

     if not accounts:
 
        accounts = self.accountdata.accounts
 
     for account in accounts:
 
       print("{0}".format(account.account))