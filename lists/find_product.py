def find_product(nums):
  product = []
  left = 1
  
  for value in nums:
    product.append(left) 
    left = left * value
  
  right = 1
  for i in range(len(nums) - 1, -1, -1):
    product[i] = product[i] * right 
    right = right * nums[i]
  
  
  return product
      


print(find_product([1, 2, 3, 4]))