'''
1. Two Sum
Difficulty : Easy
題目來源：https://leetcode.com/problems/two-sum/
'''

# 解法1(自己的解法)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range((i+1), len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 解法2(網友提供的解法)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]