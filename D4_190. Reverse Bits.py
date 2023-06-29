"""Link=https://leetcode.com/problems/reverse-bits/
solved- Q- Reverse bits of a given 32 bits unsigned integer."""

#---CODE---
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result =result<< 1 # dummy variable to store reverse binary
            last_bit=n%2
            result=result+last_bit
            
            n=n>>1 #n binary is going towards right and we are taking the last bit and adding to result
        return result