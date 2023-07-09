"""Link:https://leetcode.com/problems/majority-element/
Solved with disctionaries
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array."""
#----CODE----
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        m=defaultdict(int)
        n=l//2
        for x in nums:
            m[x]=m[x]+1
            
        for key, value in m.items():
            if value>n:
                return key
        return 0
    #another approach is to sort the array and find the n/2th element which will be the mjority element