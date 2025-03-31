from Stack import Stack

def next_greater_element(lst):
  stack_obj = Stack()
  res = [-1] * len(lst)
  for i in reversed(range(len(lst))):
    while stack_obj.is_empty() is False and stack_obj.peek() <= lst[i]:
      stack_obj.pop()
    
    if not stack_obj.is_empty():
      res[i] = stack_obj.peek()
    stack_obj.push(lst[i])
  
  return res


lst = [2,6,6,19,11,2,1,12,15]
print(next_greater_element(lst))