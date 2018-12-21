##===============================================
##   Jiadong Mai (20557203)
##   CS 234 Spring 2018
##   Assignment 01, Question 2
##===============================================

from credit import Credit

_ERR_MSG_ = "Bad transaction: {0}"

# update_accounts(credit, filename) that applies all operations in the named text
#          file, to the Credit object credit. 
# update_accounts: Credit (listof Str) -> None
# effects: mutedted the Credit follow the filename words
def update_accounts(credit, filename):
  input_file = open(filename, "r")
  text = input_file.readlines()
  input_file.close()
  for i in text:
    list_tra = i.split()
    if list_tra[0] == "open":
      cc = int(list_tra[1])
      limit = int(list_tra[2])      
      if not(credit.add_card(cc, limit)):
        print(_ERR_MSG_.format(" ".join(list_tra)))      
      else:
        credit.add_card(cc, limit)
      
      
    if list_tra[0] == "charge":
      cc = int(list_tra[1])
      amnt = int(list_tra[2])      
      desc = list_tra[3]      
      if credit.charge(cc, amnt, desc):
        a = 2
      else:
        print(_ERR_MSG_.format(" ".join(list_tra)))
      
      
      
      
    
    if list_tra[0] == "payment":
      cc = int(list_tra[1])
      amnt = int(list_tra[2])       
      if not(c.__contains__(cc)):
        print(_ERR_MSG_.format(" ".join(list_tra)))      
      else:
        credit.payment(cc, amnt)
      
  
c = Credit()
update_accounts(c, "transactions.txt")
list(c)
c.balance(0)
c.transactions(0)

