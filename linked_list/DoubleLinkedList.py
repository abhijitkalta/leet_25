class Node:
  def __init__(self, data):
    self.data = data
    self.next_element = None
    self.previous_element = None

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  def get_head(self):
    if self.head is None:
      return False
    else:
      return self.head.data
  
  def is_empty(self):
    if self.head is None:
      return True
    else:
      return False
  
  def insert_tail(self, element):
    tmp_node = Node(element)
    if self.is_empty():
      self.head = tmp_node
      self.tail = tmp_node
    else:
      self.tail.next_element = tmp_node
      tmp_node.next_element = None
      tmp_node.previous_element = self.tail
      self.tail = tmp_node
    self.length += 1
    return tmp_node.data
  
  def remove_head(self):
    if self.is_empty():
      return None
    tmp_node = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = tmp_node.next_element
      tmp_node.next_element = None 
      self.head.previous_element = None
    self.length -= 1
    return tmp_node.data
  
  def tail_node(self):
    if self.is_empty():
      return False
    else:
      return self.tail.data

  def print_list(self):
    if self.is_empty():
      print('List is empty')
      return False
    else:
      tmp_node = self.head
      while tmp_node.next_element is not None:
        print(tmp_node.data, end='->')
        tmp_node = tmp_node.next_element
      print(tmp_node.data,'->None')
      return True
    
if __name__ == '__main__':
  double_list = DoubleLinkedList()  
  for i in range(10):
    double_list.insert_tail(i)
  double_list.print_list()
  double_list.remove_head()
  print('Remove head:')
  double_list.print_list()