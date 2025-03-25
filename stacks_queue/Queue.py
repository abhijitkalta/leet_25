from DoubleLinkedList import DoubleLinkedList

class MyQueue:
  def __init__(self):
    self.items = DoubleLinkedList()
  
  def is_empty(self):
    return self.items.length == 0
  
  def front(self):
    if self.is_empty():
      return None
    else:
      return self.items.get_head()
  
  def rear(self):
    if self.is_empty():
      return None
    else:
      return self.items.tail_node()
  
  def size(self):
    return self.items.length
  
  def enqueue(self, data):
    return self.items.insert_tail(data)
  
  def dequeue(self):
    return self.items.remove_head()
  
  def print_list(self):
    return self.items.print_list()

if __name__ == "__main__" :
  queue_obj = MyQueue()
  print("queue.enqueue(2);")
  queue_obj.enqueue(2)
  print("queue.enqueue(4);")
  queue_obj.enqueue(4)
  print("queue.enqueue(6);")
  queue_obj.enqueue(6)
  print("queue.enqueue(8);")
  queue_obj.enqueue(8)
  print("queue.enqueue(10);")
  queue_obj.enqueue(10)
    
  queue_obj.print_list()

  print("is_empty(): " + str(queue_obj.is_empty()))
  print("rear(): " + str(queue_obj.rear()))
  print("front(): " + str(queue_obj.front()))
  print("size(): " + str(queue_obj.size()))
  
  