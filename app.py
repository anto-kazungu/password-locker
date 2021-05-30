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