# finding the sum of array

# def sum_of_array(arr,n):
#     if n == 0:
#         return 0
#     else:
#         return arr[n-1]+ sum_of_array(arr, n-1)

# a = [1,2,3,4,5]
# r = sum_of_array(a,len(a))
# print(r)

# findinding factorials

# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)

# n = fact(4)
# print(n)


# finding the last element in fibonacci 

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# s = int(input("\n Enter a limit of the fibonacci series:"))
# for i in range(s):
#     print(fib(i), end=' ')


# # multiply all nums in a list

# def mmul_nums(arr,n):
#     if n == 0:
#         return 1
#     else:
#         return arr[n-1] * mmul_nums(arr, n-1)

# m = [23,1,3,4]
# ans = mmul_nums(m,len(m))
# print(ans)


# sum of array

# def sum_array(arr,n):
#     if n == 0:
#         return 0
#     else:
#         return arr[n-1]+sum_array(arr, n-1)

# a = [23,1,3,4]
# ans = sum_array(a,len(a))
# print(ans)

# dividing the elements by adjacent element using recursion

# def divide_adjacent(arr,n):
#     if n == 1:
#         return [arr[0]]
#     elif n == 0:
#         return []
#     else:
#         return [arr[0]/arr[1]] + divide_adjacent(arr[1:],n - 1)


# s= [23,1,3,4]
# ans = divide_adjacent(s,len(s))
# print(ans)

# import re
# # check wether a senctence or word is palindrom
# def is_palindrome(s):
#     cleaned = re.sub(r'[^A-Za-z0-9]','',s).lower()

#     def helper(cleaned, left, right):
#         if left >= right:
#             return True
        
#         if cleaned[left] != cleaned[right]:
#             return False
        
#         return helper(cleaned, left+1,right-1)
    
#     return helper(cleaned,0,len(cleaned)-1)

# sentence = "A man, a plan, a canal: Panama!"
# print(is_palindrome(sentence))


# print even numbers
# def print_even_no(arr, n = 0):
#     if n == len(arr):
#         exit()
#     if arr[n] % 2 == 0:
#         print(arr[n], end = ' ')
    
#     print_even_no(arr, n+1)

# list1 = [2,45,32,6,7,19,10]
# print_even_no(list1)


# print prime numbers from the list
# def print_prime_num(arr):
#     prime_numbers = []
    
#     for num in arr:
#         if num > 1:  # Check if number is greater than 1
#             is_prime = True
#             for i in range(2, int(num**0.5)+ 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 prime_numbers.append(num)
    
#     print("Prime numbers in the list:", prime_numbers)

# a = [37,23,10,11,2,3,4,5,6,88,90]
# print_prime_num(a) 


# print prime numbers from the list using recursion
# def is_prime(arr, n):
#     if n == 0:
#         return []
    
#     flag = True
#     if arr[0] > 1:
#         for i in range(2, int(arr[0]**0.5) + 1):
#             if arr[0] % i == 0:
#                 flag = False
#                 break
#         if flag:
#             return [arr[0]] + is_prime(arr[1:], n - 1)
    
#     return is_prime(arr[1:], n - 1)



# a = [37,23,10,11,2,3,4,5,6,88,90]
# print(is_prime(a,len(a))) 

# check whether a number is prime or not:
# def is_prime(num):
#     if num > 1:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#     else:
#         return False
#     return True

# n = 11

# if is_prime(n):
#     print("The number is prime")
# else:
#     print("The number is not prime")


# check whether a number is prime or not: (Recursion)
# def is_prime(num, divisor = None):
#     if num <= 1:
#         return False
#     if divisor is None:
#         divisor = int(num**0.5)
#     if divisor < 2:
#         return True
#     if num % divisor == 0:
#         return False
#     return is_prime(num,divisor-1)

# n = 1

# if is_prime(n):
#     print("The number is prime")
# else:
#     print("The number is not prime")


# remove duplicate from the list:
# def remove_dup(num):
#     seen = set()
#     u = []
#     for i in num:
#         if i not in seen:
#             u.append(i)
#             seen.add(i)
#     return u

# a = [1,2,3,1,4,2,5,8,6,9,8,0,5]
# print(remove_dup(a))

# remove duplicate from list using recursion
# def remove_dup(num, seen = None):
#     if seen is None:
#         seen = set()
#     if not num:
#         return []
    
#     if num[0] not in seen:
#         seen.add(num[0])
#         return [num[0]] + remove_dup(num[1:],seen)
#     else:
#         return remove_dup(num[1:],seen)

# a = [1,2,3,1,4,2,5,8,6,9,8,0,5]
# print(remove_dup(a))

#  finding the maximum element in a  list
# def max_ele(num,n):
#     max_el = num[0]
#     i=1
#     while i < n:
#         if num[i] > max_el:
#             max_el = num[i]
#         i += 1
    
#     return max_el

# a = [1,2,3,1,4,2,5,8,6,9,8,0,5]
# print(max_ele(a,len(a)))

# finding the maximum element in a  list using recursion
# def max_ele(num,n):
#     if n == 1:
#         return num[0]
#     else:
#         return max(num[n-1], max_ele(num, n-1))
    
# a = [1,2,3,1,4,2,5,8,6,9,8,0,5]
# print(max_ele(a,len(a)))


# finding the minimum element in a  list using recursion
# def min_ele(num,n):
#     if n == 1:
#         return num[0]
#     else:
#         return min(num[n-1], min_ele(num, n-1))
    
# a = [1,2,3,1,4,2,5,8,6,9,8,0,5]
# print(min_ele(a,len(a)))


# find the first non repeating number in an array
# def first_non_repeat_no(arr, count = None, index = 0):
#     if count is None:
#         count = {}
#         for num in arr:
#             if num in count:
#                 count[num] +=1
#             else:
#                 count[num] = 1
    
#     if index == len(arr):
#         return None  # everything is repeating
    
#     if count[arr[index]] == 1:
#         return arr[index]
    
#     return first_non_repeat_no(arr,count,index+1)

# arr = [1,2,3,3,1,4,2,5,8,6,9,8,0,5]
# print(first_non_repeat_no(arr))

# binary search recursion programming:
def binary_search(arr,target):
    def search(arr, target, left, right):
        if left > right:
            return -1
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(arr, target, mid+1,right)
        else:
            return search(arr, target, left, mid-1)
    
    return search(arr, target, 0, len(arr) - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
print(binary_search(arr, target))



#  binary search without recursion


