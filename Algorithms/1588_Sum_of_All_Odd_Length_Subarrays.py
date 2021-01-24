'''
1588. Sum of All Odd Length Subarrays
Difficulty : Easy
題目來源：https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
'''

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        # 計算總數
        total = 0
        
        for pickNums in range(len(arr) + 1)[1::2]:  # 要選取的數量
            for startSite in range(len(arr)):       # 起始的位置
                
                # 先選起始位置 再選要取的數量
                newArr = arr[startSite:][:pickNums]
                
                # 長度要符合選取數量才相加
                if len(newArr) == pickNums:
                    total = total + sum(newArr)
        return total