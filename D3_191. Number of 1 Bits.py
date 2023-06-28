"""Link: https://leetcode.com/problems/number-of-1-bits/
USING FORMULA- N&(N-1)-- DIDN'T GOT ANSWER
Q-Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        i=0
        
        while i<32:
            if (n&(n-1))==1:
                count=count+1
                print(count)
            i=i+1
            
        return count