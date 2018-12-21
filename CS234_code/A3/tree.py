
class BTNode:
  '''Fields - Item - Any
              Left,Right (anyof BTNode None)'''
  # BTNode(item,left,right) returns a new Node that holds item, and has children
  #  left and right
  # __init__: BTNode Any (anyof BTNode None) (anyof BTNode None) -> None
  def __init__(self,item,left,right):
    self.item = item
    self.left = left
    self.right = right
  
  # repr(self) returns a Python-readable representation of self
  # requires: no cycles (self is not a decendent of itself)
  def __repr__(self):
    return "BTNode({!r}, {!r}, {!r})".format(self.item,self.left,self.right)
        
# Here are the example trees         
A = None
B = BTNode(1, BTNode(6,None,None), BTNode(3, None, None))
C = BTNode(1, None, BTNode(2, None, BTNode(3,None,None)))

# traverse(root) return a sorted list that contain all the node in root 
#                by consumes a BTNode
# traverse: BTNode -> (listof Int)
def traverse(root):
  current = root
  a = []
  result = []
  done = 0
  if root ==None:
    return result
  
  while (not done):
    if current is not None:         
      a.append(current)
      current = current.left
    else:
      if(len(a) > 0):
        current = a.pop()
        if current is not None:
          result.append(current.item)
        current = current.right
      else:
        if current is not None:
          result.append(current.item)
        done = 1
  return result
   
# height(root) return the hight of the BTNode by consuming a BTNode, root
# height: BTNode -> Int
def height(root):
  if root == None:
    return 0
  return max(height(root.left), height(root.right)) +1

# balanced(root) return True is the BTNode is balanced, else, return False
# balanced: BTNode -> Bool
def balanced(root):
  if root == None:
    return True
  if abs(height(root.left) - height(root.right)) <= 1:
    return balanced(root.left) and balanced(root.right)
  else:
    return False
  
   