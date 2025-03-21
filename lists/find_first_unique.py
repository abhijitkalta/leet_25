def find_first_unique(nums):
  for p1 in range(len(nums)):
    p2 = 0
    while(p2 < len(nums)):
      if p1 != p2 and nums[p1] == nums[p2]:
        break
      p2 += 1
    
    if p2 == len(nums):
      return nums[p1]
  return None