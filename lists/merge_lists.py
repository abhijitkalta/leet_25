def merge_lists(nums1, nums2):
  res = [None] * (len(nums1) + len(nums2))
  p1 = 0
  p2 = 0
  p3 = 0
  
  while p1 < len(nums1) and p2 < len(nums2):
    if nums1[p1] <= nums2[p2]:
      res[p3] = nums1[p1]
      p1 += 1
      p3 += 1
    else:
      res[p3] = nums2[p2]
      p2 += 1
      p3 += 1
  
  while p1 < len(nums1):
    res[p3] = nums1[p1]
    p1 += 1
    p3 += 1
  
  while p2 < len(nums2):
    res[p3] = nums2[p2]
    p2 += 1
    p3 += 1
  
  return res

print(merge_lists([1,2,3] , [4,5,6]))
print(merge_lists([-1,3] , [-1,-1,0,0,1,2]))
      
    
