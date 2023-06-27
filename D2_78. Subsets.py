""" Link-https://leetcode.com/problems/subsets/
WRONG ANSWER COULDN'T SOLVE (POWER SET QUESTION)
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order."""

#CODE-
class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        arr1=[]
        arr.append(arr1)
        for x in range(len(nums)+1):
            for y in range (x):
                arr1.append(nums[y])
        arr.append(arr1)        
                
        return arr
