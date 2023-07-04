"""Link:https://leetcode.com/problems/find-greatest-common-divisor-of-array/
SOLVED
Q: Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers."""

#-----CODE-----
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        res=gcd(a,b)
        return res
    
    def gcd(a,b):
        if b==0:
            return a
        else:
            return (b,a%b)