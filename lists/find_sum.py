def find_sum(nums, k):
  nums.sort()
  left = 0
  right = len(nums) - 1

  res = []
  while left < right:
    if nums[left] + nums[right] < k:
      left += 1
    elif nums[left] + nums[right] > k:
      right -= 1
    else:
      res.extend([nums[left], nums[right]])
      return res
  
  return []
    