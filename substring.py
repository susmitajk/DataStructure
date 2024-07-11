import re
def isPalindrome(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]','',s)
    return s == s[::-1]
    
str1 = "A man, a plan, a canal: Panama"
print(isPalindrome(str1)) 