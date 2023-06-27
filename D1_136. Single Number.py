"""Link - https://leetcode.com/problems/single-number/
DAY-1-Q. Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space."""

#----CODE-----
class Solution(object):
    def singleNumber(self, nums):
        xor=0
        for x in nums:
            xor=xor^x
        return xor

#NOTE--
# a^a=0 
# a^b^a=b 
