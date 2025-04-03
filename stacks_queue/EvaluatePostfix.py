from Stack import Stack
  
def evaluate_post_fix(exp):
  stack = Stack()
  res = 0
  for val in exp:
    if val.isdigit() is True:
     stack.push(int(val))
    else:
       right = stack.pop()
       left = stack.pop()
       if val == '+':
         res = right  + left 
       elif val == '-':
         res = left - right
       elif val == '*':
         res = left * right
       else:
         res =  left // right
       stack.push(res)
  
  return stack.pop()

if __name__ == '__main__':
  print(evaluate_post_fix("34*2+"))
  print(evaluate_post_fix("82/3+"))
  print(evaluate_post_fix('1693/-*')) 
  print(evaluate_post_fix('1693/+*')) 