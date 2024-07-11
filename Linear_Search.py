# def missing_numbers(arr):
#     min_val = min(arr)
#     max_val = max(arr)
#     expected_sum = sum(range(min_val,max_val+1))
#     actual_sum = sum(arr)
#     return expected_sum - actual_sum

# a = [3,0,1]
# print(missing_numbers(a)) # Output: 2

'''
The below approach only works when the array is supposed to 
contain all numbers from 0 to n, where n is the length of the array. 
In the above case (code) where the numbers are not guaranteed to start from 0 or 1, 
a different approach is needed.
'''

def missing_numbers(arr):
    n = len(arr)
    total_sum = (n*(n+1))//2
    arr_sum = sum(arr)
    return total_sum - arr_sum


a = [3,0,1]
print(missing_numbers(a))


