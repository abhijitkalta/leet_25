from Node import Node

class LinkedList:
  def __init__(self):
    self.head_node = None
  
  def get_head(self):
    return self.head_node
  
  def insert_at_head(self, data):
    tmp_node = Node(data)
    tmp_node.next_element = self.head_node
    self.head_node = tmp_node
    return self.head_node
  
  def insert_at_tail(self, data):
    if self.is_empty():
      tmp_node = Node(data)
      self.head_node = tmp_node
      return self.head_node
    else:
      tmp = self.head_node
      while tmp.next_element is not None:
        tmp = tmp.next_element
      tmp_node = Node(data)
      tmp.next_element = tmp_node
      return self.head_node
  
  def is_empty(self):
    if self.head_node:
      return False
    else:
      return True
    
  def search(self, data):
    if self.is_empty():
      return False
    else:
      tmp_node = self.head_node
      while tmp_node.next_element is not None:
        if tmp_node.data == data:
          return True
        tmp_node = tmp_node.next_element
      if tmp_node.data == data:
        return True
      else:
        return False
  
  def print_list(self):
    if self.is_empty():
      print('List is empty')
      return False
    else:
      tmp_node = self.head_node
      while tmp_node.next_element is not None:
        print(tmp_node.data, end='->')
        tmp_node = tmp_node.next_element
      print(tmp_node.data,'->None')
      return True
      
  
lst = LinkedList()
print(lst.is_empty())

print('Inserting values in linked list')
for i in range(10):
  lst.insert_at_head(i)
lst.print_list()

lst.insert_at_tail(25)
lst.print_list()
print(lst.search(7))
print(lst.search(21))

lst1 = LinkedList()
lst1.insert_at_tail(23)
lst1.print_list()