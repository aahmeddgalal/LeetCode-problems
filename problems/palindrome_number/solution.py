class Solution:
    def isPalindrome(self, x: int) -> bool:
        # res = []
        # if x < 0:
        #     return False
        
        # for i in str(x):
        #     res.insert(0, i)
        
        # new_number = ""
        # for i in res:
        #     new_number += i
        
        # if x == int(new_number):
        #     return True
        # return False 

        rev = 0
        temp = x
        if x < 0:
            return False

        while temp != 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        
        return rev == x
        