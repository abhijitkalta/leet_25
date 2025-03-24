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
  
  def delete_at_head(self):
    first_element = self.get_head()
    if first_element is not None:
      self.head_node = first_element.next_element
      first_element.next_element = None
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
  
  # def delete_value(self, data):
   
  #   if self.is_empty():
  #     return False
  #   else:
  #     tmp_node = self.get_head()
  #     if tmp_node.data == data:
  #       self.head_node = tmp_node.next_element
  #       tmp_node.next = None
  #       return True
  #     while tmp_node.next_element is not None:
  #       if tmp_node.next_element.data == data:
  #         tmp_node.next_element = tmp_node.next_element.next_element
  #         return True
  #       tmp_node = tmp_node.next_element

  #     if tmp_node.data == data:
  #       tmp_node = None
  #       return True
  #     else:
  #       return False
      
  def delete_value(self, value):
    previous = None
    deleted = False
    current = self.get_head()

    if current.data == value:
      self.head_node = current.next_element
      deleted = True
      current = None
      return deleted
    
    while current is not None:
      if current.data == value:
        previous.next = current.next
        current.next = None
        deleted = True
        break
      previous = current
      current = current.next
    
    return deleted
  
  def get_length(self):
    current = self.get_head()
    length = 0
    while current is not None:
      length += 1
      current = current.next_element
    return length
  
  def find_mid(self):
    current = self.get_head()
    length = self.get_length()
    mid, i = 0, 0
    if length%2==1:
      mid = length//2 + 1
    else:
      mid = length//2 + 1
    while i < mid:
      res = current.data
      current = current.next_element
      i += 1
    return res
    
  
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

lst.delete_at_head()
lst.print_list()

print('Delete value 8')
print(lst.delete_value(8))
lst.print_list()
print(lst.get_length())

print('Mid', lst.find_mid())

lst1 = LinkedList()
lst1.insert_at_tail(23)
lst1.print_list()