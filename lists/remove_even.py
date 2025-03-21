def remove_even(lst):
  res = []
  for i in lst:
    if i%2 != 0:
      res.append(i)
  return res

print(remove_even([1, 5, 4, 3, 2]))