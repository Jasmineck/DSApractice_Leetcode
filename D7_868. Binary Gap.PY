"""
Link:https://leetcode.com/problems/binary-gap/
SOLVED
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 """
 #---CODE---
class Solution:
    def binaryGap(self, n: int) -> int:
        new=bin(n)[2::]
        bi=[]
        l=len(new)
        for x in range(l):
            if new[x]=="1":
                bi.append(x)
        bi.sort()
        max=0
        l=len(bi)-1
        for y in range(l):
            c=bi[y+1]-bi[y]
            if max<c:
                max=c
        return max
            
            
        
