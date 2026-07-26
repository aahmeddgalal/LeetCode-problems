import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return "Can't be Negative"
        return math.floor(sqrt(x))

        # if x < 2:
        #     return x
        
        # left, right = 1, x

        # while left <= right:
        #     mid = (left + right) // 2
        #     square = mid * mid

        #     if square == x:
        #         return mid
        #     elif square > x:
        #         right == mid - 1
        #     elif square < x:
        #         left == mid + 1

        # return right