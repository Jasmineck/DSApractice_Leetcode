"""Link=https://leetcode.com/problems/single-number-iii/"""
#Couldn't solve
"""Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space."""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=0
        resuly=[0,0]
        nums=nums.sort()
        for x in nums:
            res=res^x
        res=res&(-res)
        for y in nums:
            if(res&y):
                result[0]=result[1]^y
            else:
                result[0]=result[0]^y
            
        return result