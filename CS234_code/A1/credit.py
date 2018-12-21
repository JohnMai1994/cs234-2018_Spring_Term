##===============================================
##   Jiadong Mai (20557203)
##   CS 234 Spring 2018
##   Assignment 01, Question 1
##===============================================

# CS234 A1 Q1 Starter File
# Don't forget to put your header up here!
# Also:  Don't forget to complete missing components of the design recipe!

def check (num):
  length = len(str(num))
  all_num = 0
  for i in range(length-1):
        all_num = all_num + int(str(num)[i])
  
  if all_num %10 == num%10:
    return True
  else:
    return False  


class Credit:
  """Used to keep track of account information for issued credit cards"""
  
  # Credit() returns a newly created (and empty) Credit object
  # __init__: None -> Credit
  def __init__(self):
    self.credit_num = {}
    
  
  # (cc in self) returns true if and only if there is a card in self with number cc
  # __contains__: Nat -> Bool
  def __contains__(self,cc):
    if (cc in self.credit_num):
      return True
    else:
      return False
  
  # for v in self: iterates through all credit card numbers in self, in 
  #    ascending order
  #__iter__: None -> <FILL IN WITH WHATEVER YOU NAME YOUR ITERATOR CLASS>
  def __iter__(self):
    return _Iterator_(list(self.credit_num.keys()))
   
  # len(self) returns the number of credit cards currently in self
  #__len__: None -> Nat
  def __len__(self):
    return len(self.credit_num) 
  
  # self.add_card(cc,limit) adds a card with the given card number and credit 
  #   limit to the Credit object.
  #   return value indicates success.  Fails if cc is not a valid credit card 
  #   number, or if Credit object already contains that number
  # add_card: Nat Nat -> Bool
  # require: cc is a credit number
  # effects: a credit card called cc is added
  
  def add_card(self,cc,limit):
    if check(cc) and (cc not in self.credit_num):
      balance = 0
      self.credit_num[cc] = [limit, balance, []]
      return True
    else:
      return False
  
  # self.limit(cc) returns the credit limit on for card cc 
  # limit: Nat -> Nat
  
  def limit(self,cc):
    return self.credit_num[cc][0]
  
  # self.balance(cc) returns the balance owing on the card with number cc
  # balance: Nat -> Int
  def balance(self,cc):
    return self.credit_num[cc][1]

  # self.charge(cc,amnt,desc) charges amnt cents to the card with number cc, 
  #   and using desc as the description that will appear on the bill.  
  #  Returns True on success, False on failure (if the charge will exceed the 
  #    card's limit)
  # charge: Nat Nat String -> Bool
  # require: cc is a member of self
  # effects: the balace of the cc credit card is mutated 
  def charge(self,cc,amnt,desc):
    assert (cc in self.credit_num)
    if self.credit_num[cc][1] + amnt > self.credit_num[cc][0]:
      return False
    else:
      self.credit_num[cc][1] += amnt
      self.credit_num[cc][2].append([amnt, desc])
      return True
  
  #  self.payment(cc,amnt) registers a payment of amnt cents toward the balance 
  #    owing on card cc
  # payment: Nat Nat -> None
  # require: cc is a member of self
  # effects: the balace of the cc credit card is mutated   
  def payment(self,cc,amnt):
    if (cc in self.credit_num):
      self.credit_num[cc][1] -= amnt
      self.credit_num[cc][2].append([-amnt, "Payment"])
    else:
      return False
    
  
  # self.reissue(cc,cc_new) changes the card number of card cc to be cc_new.
  # reissue: Nat Nat -> None
  # require: cc is a member of self
  # effects: the name of the cc credit card is mutated to cc_new  
  def reissue(self,cc,cc_new):
    self.credit_num[cc_new] = self.credit_num.pop(cc)

  # self.transactions(cc) returns a list of the 10 most recent transactions for 
  #     card cc.  
  #  transactions: Nat -> (listof (list Int Str))           
  
  def transactions(self,cc):
    if len(self.credit_num[cc][2]) > 10:
      return self.credit_num[cc][2][::-1][0:10]
    else:
      return self.credit_num[cc][2][::-1]
    

    

    

class _Iterator_:
  # _Iterator_(items) returns an iterator that traverses the values in items
  # __init__: _Iterator_ (listof Any) -> None
  def __init__(self,items):
    self._items_ = items
    self._pos_ = 0
  
  # iter(self) returns self (since self is already an iterator)
  # __iter__: _Iterator_ -> _Iterator_
  def __iter__(self):
    return self
  
  # next(self) returns the next item if there is one, otherwise
  #            raises the StopIteration exception
  # __next__: Iterator_ -> Any
  def __next__(self):
    if self._pos_ < len(self._items_):
      rv = self._items_[self._pos_]
      self._pos_ += 1
      return rv
    else:
      raise StopIteration



# __public_test__() asserts the example interactions from the assignment 
#     description
#   If nothing happens, you passed!  If an assertion fails, you failed!
def __public_test__():
  c = Credit()
  assert 0 == len(c) # uses __len__
    
  assert [] == list(c) # uses __iter__
  c.add_card(0,50000) # 0 is a valid card number
  assert c.charge(0,10000, 'foo')
  assert not c.charge(0,45000, 'bar') # over the limit
  c.payment(0,10000)
  assert c.charge(0, 45000, 'bar')
    
  assert c.transactions(0) == [[45000,'bar'], [-10000, 'Payment'], [10000, 'foo']], c.transactions(0)
  assert 0 in c # uses __contains__
  assert 8675309 not in c 
  loop_values = []
  for ccn in c: # uses __iter__
    loop_values.append([ccn,c.balance(ccn)])
  assert loop_values == [[0,45000]]
  c.reissue(0,11) # 11 is also a valid number
  assert 1 == len(c)
  assert 50000 == c.limit(11)
