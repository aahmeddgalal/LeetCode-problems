class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hmap = {} # index: value
        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_hmap:
                return [my_hmap[diff], i]
            my_hmap[num] = i