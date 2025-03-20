def is_strobogrammatic(num):
  valid_num = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
  }
  
  res = list(num)
  left = 0
  right = len(res) - 1

  while left <= right:
    if res[left] not in valid_num or valid_num[res[left]] != res[right]:
      return False
    left += 1
    right -= 1

  return True

print(is_strobogrammatic('619'))  # Example usage
