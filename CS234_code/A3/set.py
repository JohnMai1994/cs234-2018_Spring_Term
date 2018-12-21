
INIT_SIZE = 16
ALPHA_TRIG = 2/3



class Set:
  
  # Set() returns an empty Set
  # __init__: Set -> None
  def __init__(self):
    self.count = 0
    self.size = 16    
    self.alpha_trig = 2/3
    self.capacity = [None] * self.size
      
  
  # item in self returns True if item is a member of the set Self, else False 
  # __contains__: Set Any -> Bool
  def __contains__(self, item):
    if self.count == 0:
      return False
    for i in self.capacity:
      if i == item:
        return True
    return False
  
  # len(self) returns the number of values currently in self
  # __len__: Set -> Nat
  def __len__(self):
    length = 0
    for i in self.capacity:
      if (i != None) :
        length = length + 1
    return length
  
  # add(self, v) adds the number v to self, and resize when the load factor 
  #    exceeds 2/3, by consuming self and v
  # add: Set Nat -> None
  def add(self,v):
    pos = hash(v) % self.size
    if (self.capacity[pos] == v):
      return None
    
    while (self.capacity[pos] != None):
      pos = hash(pos) % self.size + 1
    
    self.capacity[pos] = v
    self.count = self.count + 1
    
    if (self.count >= self.alpha_trig * self.size):
      self.size = (2 * self.size)
      new_list = [None] * self.size
      
      for i in self.capacity:
        if i != None:
          new_pos = hash(i) % self.size
          while (new_list[pos] != None):
            new_pos = hash(new_pos) % self.size + 1
          new_list[new_pos] = i
        
      self.capacity = new_list
          
  # remove(self, v) remove the number v from self by consuming self and v
  # remove: Set Nat -> None
  def remove(self,v):
    pos = hash(v)% self.size
    while (self.capacity[pos] != v):
      if self.capacity[pos] == None:
        raise ValueError("Can't find the value")
      pos = hash(pos) % self.size + 1
      
    self.capacity[pos] = None
    
  
  # union(self, other) return a new set which combina two set, self and 
  #                    other, together by consuming self and other
  # union: Set Set -> Set
  # Require: 
  #   self and other should be Set or None  
  def union(self,other):
    new_union = Set()
    for i in other.capacity:    # first loop to put the element in other into
      new_union.add(i)          #  the set of new_union O(m)
      
    for k in self.capacity:     # second loop to put the element in self into
      if k not in new_union.capacity: # the set of new_union O(n)
        new_union.add(k)
    
    return new_union
  
  # intersection(self, other) return a new set which contains all elements that
  #                           are in both sets, by consuming self and other
  # intersection: Set Set -> Set
  # Require: 
  #   self and other should be Set or None  
  def intersection(self,other):
    new_intersection = Set()
    for i in self.capacity:
      if i in other.capacity:
        new_intersection.add(i)
    return new_intersection
  
  # subtract(self, other) return a new set that the elements in self but not 
  #                       in the other by consuming self and other
  # subtract: Set Set -> Set
  # Require: 
  #   self and other should be Set or None
  def subtract(self,other):
    new_subtract = Set()          
    for i in self.capacity:       # loop for all element in self: O(n)
      if i not in other.capacity: #   if statement, which is O(1)
        new_subtract.add(i)       #         add operation    O(1)
    return new_subtract          
  

    
a = Set()
a.add(5)
a.add(1)
a.add(3)
a.add(2)
a.add(6)
a.add(7)
a.add(8)
a.add(9)
a.add(10)
a.add(11)
a.add(22)
a.add(13)

