
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