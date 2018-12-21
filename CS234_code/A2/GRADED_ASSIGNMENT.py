ASSIGNMENT a02
Student's Quest ID: j4mai

*******************************************************************************
**** Testing Results **********************************************************

12/20   Total Mark

 ** Question 1: 12/20

(Question 1, Test t01, 1 marks): Index test: positive: Passed; passed.
(Question 1, Test t02, 1 marks): Index test: negative: Passed; passed.
(Question 1, Test t03, 1 marks): Containment test: Passed; passed.
(Question 1, Test t04, 1 marks): Length test: Passed; passed.
(Question 1, Test t05, 1 marks): Method: add_front: Passed; passed.
(Question 1, Test t06, 1 marks): Method: add_back: Passed; passed.
(Question 1, Test t07, 1 marks): Method: remove_front: general: Passed;
    passed.
(Question 1, Test t08, 1 marks): Method: remove_front: complex: FAILED;
    FAILED: exception occurred: AttributeError: 'NoneType' object has no at-
    tribute 'prev'
(Question 1, Test t09, 1 marks): Method: remove_back: general: Passed; passed.
(Question 1, Test t10, 1 marks): Method: remove_back: complex: FAILED; FAILED:
    exception occurred: AttributeError: 'NoneType' object has no attribute
    'next'
(Question 1, Test t11, 1 marks): Stack test: FAILED; FAILED: exception oc-
    curred: AttributeError: 'NoneType' object has no attribute 'prev'
(Question 1, Test t12, 1 marks): Queue test: FAILED; FAILED: exception oc-
    curred: AttributeError: 'NoneType' object has no attribute 'prev'
(Question 1, Test t13, 1 marks): Remove test: general: Passed; passed.
(Question 1, Test t14, 1 marks): Remove test: edges: FAILED; FAILED: exception
    occurred: AttributeError: 'NoneType' object has no attribute 'prev'
(Question 1, Test t15, 1 marks): Sort test: general: Passed; passed.
(Question 1, Test t16, 1 marks): Sort test: edges: FAILED; FAILED: exception
    occurred: AttributeError: 'NoneType' object has no attribute 'prev'
(Question 1, Test t17, 1 marks): Efficiency test: length: FAILED; FAILED: got
    False expected True
(Question 1, Test t18, 1 marks): Efficiency test: add: Passed; passed.
(Question 1, Test t19, 1 marks): Efficiency test: remove: Passed; passed.
(Question 1, Test t20, 1 marks): Final test: FAILED; FAILED: exception oc-
    curred: AttributeError: 'NoneType' object has no attribute 'prev'
**** End of files *************************************************************


**** sequence.py *****************************************************************

##===============================================
##   Jiadong Mai (20557203)
##   CS 234 Spring 2018
##   Assignment 02, Question 1
##===============================================

class Sequence:
  '''An ADT that is similar to a Python list, with different 
     time complexities'''
  
  # Sequence() returns a new, empty sequence
  # __init__: Sequence -> None
  
  def __init__(self):
    # head and tail are None at the beginning
    self.head = None
    self.tail = None
  
  # self[i] returns the item at index i in self
  # __getitem__: Sequence Int -> Any
  # requires: i is a valid index in self
  # time:  O(i)
  
  def __getitem__(self,i):
    front_node = self.head
    back_node = self.tail
    if i >= 0:
      while i != 0:
        front_node = front_node.next
        i -= 1
      return front_node.item
      
    if i <0:
      while i != -1:
        back_node = back_node.prev
        i += 1
      return back_node.item
  
  # self[i] = v sets the item at index i in self to have value v
  # effects: self is modified
  # __setitem__: Sequence Int Any -> None
  # requires: i is a valid index in self
  # time: O(i)
  
  def __setitem__(self,i,v):
    front_node = self.head
    back_node = self.tail
    if i >= 0:
      while i != 0:
        front_node = front_node.next
        i -= 1
      front_node.item = v
      
    if i <0:
      while i != -1:
        back_node = back_node.prev
        i += 1
      back_node.item = v
       
  
  # v in self returns True if v occurs somewhere in self, False otherwise
  # __contains__: Sequence Any -> Bool
  # time: O(n)
  
  def __contains__(self,v):
    node = self.head
    while node:
      if node.item == v:
        return True
      else:
        node = node.next
    return False
  
  # len(self) returns the length of self
  # __len__: Sequence -> Nat
  # time: O(1)
  
  def __len__(self):
    node = self.head
    k = 0
    if node == None:
      return k
    
    while node:
      if node.next == None:
        k = k + 1
        return k
      else:
        k = k + 1
        node = node.next
  
  # iter(self) returns a new iterator that traverses the items in self
  # __iter__: Sequence -> _SequenceIterator
  # time: O(1)
  
  def __iter__(self):
    return _SequenceIterator(self.head)
    # Note: This method is high priority so we an use list(seq) to 
    #       test your other methods!
  
  ## The non-magic methods are up to you to document!
  ## Please use the same contract style as above 
  ##     (i.e. include "self" in the contract)
  
  # add_front(self, v) prepends v 
  # add_front: Sequence, Int -> None
  # Effects: the Sequence was mutated
  # time: O(1)
  
  def add_front(self,v):
    new_node = DoublyLinkedNode(v, None, None)
    if self.tail is None:
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      new_node.prev = None
      self.head.pre = new_node
      self.head = new_node
      self.head.next.prev = self.head
  
  # add_back(self, v) appends v 
  # add_back: Sequence, Int -> None
  # Effects: the Sequence was mutated  
  # time: O(1)
  
  def add_back(self,v):
    new_node = DoublyLinkedNode(v, None, None)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      new_node.prev = self.tail
      new_node.next = None
      self.tail.next = new_node
      self.tail = new_node    
  
  # Note: This method is high priority as we need to be
  # able to build a Sequence before we can test your other methods!
  
  # remove_front(self) remove the first element in the Sequence
  # remove_front: Sequence -> None
  # Effects: the Sequence was mutated
  # time: O(1)
  
  def remove_front(self):
    self.head = self.head.next
    self.head.prev = None
  
  # remove_back(self,) remove the last element in the Sequence
  # remove_back: Sequence -> None
  # Effects: the Sequence was mutated  
  # time: O(1)
  
  def remove_back(self):
    self.tail = self.tail.prev
    self.tail.next = None
  
  # remove(self, v) remove the first occurrence of v in the Sequence
  # remove: Sequence -> None
  # Effects: the Sequence was mutated    
  # time: O(n)
  
  def remove(self,v):
    node = self.head
    
    while node is not None:
      if node.item == v:
        if node.prev is not None:
          node.prev.next = node.next
          node.next.prev = node.prev
        else:
          self.head = node.next
          node.next.prev = None
      node = node.next
      
  # sort(self) sort the Sequence
  # sort: Sequence -> None
  # Effects: the Sequence was mutated    
  # time: ???
  def sort(self):
    my_list = sorted(list(self))
    new_node = Sequence()
    for i in my_list:
      new_node.add_back(i)
    self.head = new_node.head
    self.tail = new_node.tail
      
    

class _SequenceIterator:
  def __init__(self,node):
    self._node = node
    
  # __iter__: SquenceIterator -> SquenceIterator
  def __iter__(self): return self
  
  def __next__(self):
    if self._node == None:
      raise StopIteration
    else:
      rv = self._node.item
      self._node = self._node.next
      return rv  




class DoublyLinkedNode:
  """Your basic linked list node
  
  Fields:
  item - Any
  prev - Node
  next - Node
  
  """
  # Note: No underscores.  This is not an ADT, just a simple object to hold
  # two values, so the fields are public
  
  
  # Node(item,next) returns a new node with the given item and next node
  # __init__: Node Any Node -> None
  def __init__(self,item,prev,next):
    self.item = item
    self.prev = prev
    self.next = next
    
  # repr(self) gives a Python representation of the Node's value
  # __repr__: Node -> Str
  def __repr__(self):
    # There's a way to tell format you want the repr of the object, but
    #   I figure I'm showing you enough new things at the moment?
    return "Node({0}, {1})".format(repr(self.item),repr(self.next))
  
  # str(self) gives a human readable representation of the linked list 
  # __str__: Node -> Str
  def __str__(self):
    node = self
    r = "["
    first = True
    while node != None:
      if not first: 
        r += ','
      else:
        first = False
      r += str(node.item)
      node = node.next
    r += ']'
    return r
  
  # iter(self) returns an iterator that traverses the values in the linked list
  #  that starts with Node self
  # __iter__: Node -> LLIterator
  def __iter__(self):
    return LLIterator(self)
      
class LLIterator:
  # LLIterator(node) returns a new iterator that traverses the values in 
  #  the linked list that starts with node
  # __init__: LLIterator Node -> None
  def __init__(self,node):
    self._node = node
    
  # __iter__: LLIterator -> LLIterator
  def __iter__(self): return self
  
  def __next__(self):
    if self._node == None:
      raise StopIteration
    else:
      rv = self._node.item
      self._node = self._node.next
      return rv
 


S = Sequence()
assert(len(S) == 0)
S.add_front(3)
S.add_back(9)
assert(S[0] == 3)
assert(S[1] == 9)
S[-1] = 0
assert(S[-1]==0)
S.add_back(12)
S.sort()
assert(list(S)==[0,3,12])
S.remove(3)
assert((3 in S) == False)


**** End of graded assignment. *************************************************
