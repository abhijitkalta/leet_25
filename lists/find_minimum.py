def find_minimum(lst):
  minimum = lst[0]
  for i in range(1, len(lst)):
    if lst[i] < minimum:
      minimum = lst[i]
  
  return minimum

print(find_minimum([2, -5, 4, 0]))
