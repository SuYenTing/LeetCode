'''
13. Roman to Integer
Difficulty : Easy
題目來源：https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # 整數最大值
        maxIntValue = 2**31
        
        # 負值肯定不是回文值 所以可以直接給false
        if x < 0 or or x%10 == 0 or x > maxIntValue-1 or x < -maxIntValue:
        
            return False
        
        else:
            
            # 處理正值回文
            popTarget= x
            palindromeValue = 0
            while popTarget != 0:
                
                pop = popTarget % 10                       # x除上10取餘數
                
                popTarget = int(popTarget / 10)            # x除上10取整數
                
                palindromeValue = palindromeValue*10+pop   # 回文值
            
            # 若原值等於回文值 則回傳true 否則為false
            return x == palindromeValue                
                