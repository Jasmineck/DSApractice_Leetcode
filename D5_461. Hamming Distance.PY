"""Link:https://leetcode.com/problems/hamming-distance/
SOLVED- Q=The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them."""

#-------CODE------

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        X=x^y
        new=bin(X)[2:]
        a=new.count("1")
        return a
        

 