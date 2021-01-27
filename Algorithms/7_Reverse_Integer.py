'''
7. Reverse Integer
Difficulty : Easy
題目來源：https://leetcode.com/problems/reverse-integer/
'''

# 自己的解法
class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 0:
            y = int(str(x)[::-1])
        else:
            y = -int(str(x)[:0:-1])
        
        if y < -2**31 or y > 2**31-1:
            y = 0
            
        return(y)
    

# 參考答案的寫法(僅處理反轉 未處理溢位問題)
x = int(-125)
rev = 0

while x != 0:

    pop = x - int(x/10) * 10   # 負數不能直接用 x/=10 會出問題!
    x /= 10
    x = int(x)
    print(x)

    temp = rev * 10 + pop
    rev = temp
    print(rev)