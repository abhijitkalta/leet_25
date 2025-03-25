class Stack:
  def __init__(self):
    self.stack_list = []
    self.stack_size = 0
  
  def is_empty(self):
    return self.stack_size == 0
  
  def push(self, data):
    self.stack_list.append(data)
    self.stack_size += 1
  
  def pop(self):
    if self.is_empty():
      return None
    else:
      self.stack_list.pop()
      self.stack_size -= 1
  
  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.stack_list[-1]
  
  def size(self):
    return self.stack_size

if __name__ == '__main__':
  stack_obj = Stack()
  print("Pushing elements into the stack")
  for i in range(5):  
      print(i)
      stack_obj.push(i)

  print("is_empty(): " + str(stack_obj.is_empty())) 
  print("peek(): " + str(stack_obj.peek()))
  print("size(): " + str(stack_obj.size()))

  print("Popping elements from the stack")
  for x in range(5):  
      print(stack_obj.pop())

  print("is_empty(): " + str(stack_obj.is_empty()))
  print("peek(): " + str(stack_obj.peek()))
  print("size(): " + str(stack_obj.size()))