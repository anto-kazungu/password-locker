#class for a single account

class Account:
 
   '''Class for account'''
 
   def __init__(self, account, username, password=' '):
 
       '''
       Initialize a new diary with memo and tags. Creation date of new notes and id are automatically set
       '''
       self.account = account
       self.username = username
       self.password = password

   def match(self, filter):
        '''
        Check match when search is done.
        '''  
        return filter in self.username or self.password

#class for all the accounts created

class allacounts:   
 
    '''
    Class for all the accounts created
    '''
 
    def __init__(self):
 
        '''
        Initialization of the allacount list
        '''
        self.accounts = []

    def new_account(self, account, username, password=''): #initialization of the account
 
       '''
       Creates the new accounts
       '''
       self.accounts.append(Account(account, username, password))
