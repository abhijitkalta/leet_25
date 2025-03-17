class LinkedListNode:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert_node_at_head(self, node):
    if self.head:
      node.next = self.head
      self.head = node
    else:
      self.head = node
  
  def create_linked_list(self, lst):
   for x in reversed(lst):
    new_node = LinkedListNode(x)
    self.insert_node_at_head(new_node) 
  
  def __str__(self):
    result = ''
    tmp = self.head
    while tmp:
      result += str(tmp.data)
      tmp = tmp.next
      if tmp:
        result += ','
    return result


lst = [2, 4, 5, 1]
linkedLst = LinkedList()
linkedLst.create_linked_list(lst)
print(linkedLst)


def remove_nth_last_node(head, n):
  right = head
  left = head
  for i in range(n):
    right = right.next
  
  if not right:
    return head.next
  
  while right.next:
    right = right.next
    left = left.next
  
  left.next = left.next.next
  return head


print(remove_nth_last_node([23,28,10,5,67,39,70,28] , 2))