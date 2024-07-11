def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize the result array with 1s
    result = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and combine with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

# Example usage
nums = [-1,1,0,-3,3]
p = productExceptSelf(nums)
print(p)