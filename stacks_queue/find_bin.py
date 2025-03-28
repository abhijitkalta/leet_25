from Queue import MyQueue
def find_bin(n):
    q   = MyQueue()
    for i in range(1, n+1):
      bin_str = str(bin(i))
      q.enqueue(bin_str[2:])
    return q

find_bin(5).print_list()