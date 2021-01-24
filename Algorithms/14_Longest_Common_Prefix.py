'''
14. Longest Common Prefix
Difficulty : Easy
題目來源：https://leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # 若有空資料則完全不用比對
        if '' in set(strs) or not strs:
            return ''
        else:
            # 欲比對字元的長度
            maxChar = min([len(elem) for elem in strs])
            # 迴圈比對
            for i in range(maxChar):
                judge = [elem[i] for elem in strs]
                if len(set(judge)) != 1:
                    i = i-1
                    break
            # 取出字串
            return strs[0][0:(i+1)]
