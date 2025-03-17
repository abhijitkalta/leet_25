def three_sum(nums):
  nums.sort()
  result = []
  n = len(nums)  
  for pivot in range(n - 2):
    if nums[pivot] > 0:
      break
    if pivot > 0 and nums[pivot] == nums[pivot - 1]:
      continue 
    left = pivot + 1
    right = n - 1
    while left < right:
      total = nums[pivot] + nums[left] + nums[right]
      if total < 0:
        left += 1
      elif total > 0:
        right -= 1
      else:
        result.append([nums[pivot], nums[left], nums[right]])
        left += 1
        right -= 1
        while left < right and nums[left] == nums[left -1]:
          left += 1
        while left < right and nums[right] == nums[right+1]:
          right -= 1
  return result


