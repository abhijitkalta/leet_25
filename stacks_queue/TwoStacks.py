class TwoStacks:
  def __init__(self, n):
    self.size = n
    self.arr = [0] * n
    self.top1 = -1
    self.top2 = self.size
  
  def push1(self, value):
    if self.top1<self.top2 -1:
      self.top1 +=1
      self.arr[self.top1] = value
    else:
      print('Stack overlfow')
      exit(1)

  def push2(self, value):
    if self.top1 < self.top2 - 1:
      self.top2 -= 1
      self.arr[self.top2] = value
    else:
      print('Stack overfow')
      exit(1)
  
  def pop1(self):
    if self.top1 >= 0:
      val = self.arr[self.top1]
      self.top1 -= 1
      return val
    else:
      print('Stack underflow')
      exit(1)
  
  def pop2(self):
    if self.top2 < self.size:
      val = self.arr[self.top2] 
      self.top2 += 1
      return val
    else:
      print('Stack underflow')
      exit(1)

if __name__ == '__main__':
  stack_obj = TwoStacks(4)
  stack_obj.push1(5)
  stack_obj.push2(10)
  stack_obj.push1(15)
  print(stack_obj.pop2())
  print(stack_obj.pop2())
  

  
    