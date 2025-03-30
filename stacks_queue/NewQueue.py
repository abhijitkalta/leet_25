from Stack import Stack

class NewQueue:
  def __init__(self):
    self.main_stack = Stack()
    self.temp_stack = Stack()
  
  def enqueue(self, value):
    if self.main_stack.is_empty() and self.temp_stack.is_empty():
      self.main_stack.push(value)
    else:
      while not self.main_stack.is_empty():
        self.temp_stack.push(self.main_stack.pop())
      
      self.main_stack.push(value)
      while not self.temp_stack.is_empty():
        self.main_stack.push(self.temp_stack.pop())
  
  def dequeue(self):
    if self.main_stack.is_empty():
      return None
    value = self.main_stack.pop()
    return value

if __name__ == '__main__':
  queue_obj = NewQueue()
  queue_obj.enqueue(3)
  queue_obj.enqueue(5)
  queue_obj.enqueue(4)
  print(queue_obj.dequeue())
