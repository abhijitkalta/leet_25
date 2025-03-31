from Stack import Stack

def sort_stack(stack):
  temp_stack = Stack()
  while stack.is_empty() is False:
    value = stack.pop()
   # If value is not none and larger, push it at the top of the temp_stack
    if temp_stack.peek() is not None and value >= temp_stack.peek():
      temp_stack.push(value)
    else:
      while not temp_stack.is_empty() and value < temp_stack.peek():
          stack.push(temp_stack.pop())
          # Place value as the smallest element in temp_stack
      temp_stack.push(value) 
  
  while not temp_stack.is_empty():
    stack.push(temp_stack.pop())
  return stack

if __name__ == "__main__":
  stack_obj = Stack()
  stack_obj.push(-31)
  stack_obj.push(13)
  stack_obj.push(-7)
  stack_obj.push(6)
  res = sort_stack(stack_obj)
  res_size = res.size()
  for i in range(res_size):
    print(res.pop())