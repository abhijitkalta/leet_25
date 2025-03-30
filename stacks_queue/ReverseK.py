from Stack import Stack
from Queue import MyQueue

def reverse_k_element(queue, k):
  if queue.is_empty() is True or k < 0 or k > queue.size():
    return None
  
  stack = Stack()
  for i in range(k):
    stack.push(queue.dequeue())
  
  while stack.is_empty() is False:
    queue.enqueue(stack.pop())
  
  size = queue.size()
  for i in range(size - k):
    queue.enqueue(queue.dequeue())
  
  return queue


if __name__ == "__main__":
    test_cases = [
        [1,2,3,4,5,6,7,8,9,10],
        [-2,1,-5,45,6,3,-9],
        [1,2,5,0,7,4,23],
        [7,3,5,6,8,12],
        [5,67,43,23,12,56,78,98,6,21,9]
    ]
    k_values = [4, 10, -7, 5, 2]
    for i in range(len(test_cases)):
        queue = MyQueue()
        for item in test_cases[i]:
            queue.enqueue(item)
        k = k_values[i]
        print(i+1, "\tOriginal Queue:", queue.print_list())
        print("\tk value:", k)
        reversed_queue = reverse_k_element(queue, k)
        print("\tQueue after reversal:" , queue.print_list())
        print("-"*100)