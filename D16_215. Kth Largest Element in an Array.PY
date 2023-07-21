"""Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Unsolved
Q-Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 
 
 
"""
#CODE----
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=nums.sort()
        #res = [*set(nums)]
        l=len(nums)
        r=nums[l-k]
        return r