from Stack import Stack

class MinStack:
  def __init__(self):
    self.min_stack = Stack()
    self.main_stack = Stack()
  
  def pop(self):
    self.min_stack.pop()
    return self.main_stack.pop()
  
  def push(self, value):
    self.main_stack.push(value)
    if self.min_stack.is_empty() or self.min_stack.peek() > value:
      self.min_stack.push(value)
    else:
      self.min_stack.push(self.min_stack.peek())
  
  def min(self):
    return self.min_stack.peek()