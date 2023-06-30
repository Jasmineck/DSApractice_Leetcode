"""Link: https://leetcode.com/problems/number-of-even-and-odd-bits/
SOLVED Q-You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd]."""

#-----CODE----

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        arr=[]
        even=0
        odd=0
        abc=bin(n)[2:]
        abc=abc[::-1]
        print(abc)
        for x in range(len(abc)):
            
            if abc[x]=="1":
                if x%2==0:
                    even=even+1
                else:odd=odd+1
                
        return [even,odd]