"""Link:https://leetcode.com/problems/two-sum/?envType=featured-list&envId=top-interview-questions
Q: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

 #CODE
 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        arr=[]
        for x in range(l):
            sum=target-nums[x]
            for y in range(x+1,l):
                if nums[y]==sum:
                    arr.append(x)
                    arr.append(y)
                    arr=list(arr)
                    return arr
            