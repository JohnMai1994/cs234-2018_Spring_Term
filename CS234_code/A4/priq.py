class Minheap:
  def __init__(self, value, priority):
    self.value = value
    self.priority = priority
    
  def __repr__(self):
    return "info: {0}, priority: {1}".format(self.value, self.priority)  
   


class PriQueue:
  # PriQueue() returns an empty priority queue
  # __init__: PriQueue -> None
  def __init__(self):
    self.que = []
  
  # len(self) returns the number of elements currently queued in self.
  # __len__: PriQueue -> Nat
  def __len__(self):
    return len(self.que)
  
  # enqueue(self, value, p) return None but mutate the self by adds value to self
  #    with priority p
  # enqueue: PriQueue Nat Nat -> None
  def enqueue(self,value,p):
    node = Minheap(value, p)
    if len(self.que) == 0:
      self.que.append(node) 
    else: 
      for i in range(0, len(self.que)):
        if node.priority >= self.que[i].priority:
          if i +1 == (len(self.que)):
            self.que.insert(i+1, node)
          else:
            continue
        else:
          self.que.insert(i,node)
          
      
  # dequeue(self) remove and return the value in self with the highest priority
  #  (the smallest value for p).
  # dequeue: PriQueue -> Nat
  def dequeue(self):
    node = self.que.pop(0)
    return node.value
  