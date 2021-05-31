
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

 #For adding new accounts to the array

 def add_account(self):
 
     ''' Add a new diary in the diarybook '''
 
     account = input("Enter a account:         " )
     username = input("Enter a username:         " )
     password = input("Enter a password:         " )
 
     self.accountdata.new_account(account, username, password)
 
     print("Your account has been added")

 #Picks the users input and use it to search the accounts
 def search_account(self):
 
     ''' Search for a specific diary in the diarybook using the match filter '''
 
     filter = input("Search for:  ")
 
     searchaccount = self.accountdata.search_account(filter)
 
     self.show_accounts(searchaccount)

 #For deleting the accounts in the list array

 def delete_account(self,accounts):

     ''' 
     Search for a specific diary in the diarybook using the match filter
     '''
     print("Enter the item you want to delete")
     name = input()
     accounts.remove(name)
     print(f'Sucessfully removed {name}')


 #Random password generator , uses the imported modules random and string
 def password_generator(self):

     ''' 
     Search for a specific diary in the diarybook using the match filter
     '''
     length = int(input('\nEnter the length of password: '))
     all = string.ascii_letters + string.digits + string.punctuation
     x = "".join(random.sample(all, length))
     print(f'Generated password is {x}')