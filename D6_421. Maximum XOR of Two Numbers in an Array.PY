"""Link:https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
couldn't solve
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n."""

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        l=len(nums)
        c=0
        max=0
        for x in range(l):
            xo=nums[x]^nums[l-c]
            if xo>=max:
                max=xo
            c=c+1
        return max
        