"""Accepted solution--Link =https://leetcode.com/problems/number-of-1-bits/submissions/"""

class Solution:
    def hammingWeight(self, n: int):
        count=0
    
        mask=1
        
        while n:
            if n&1:
                count=count+1
                
            n=n>>1
            
        return count