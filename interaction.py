
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