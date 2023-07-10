"""Link:https://leetcode.com/problems/permutations/
Solved- but had to review again(Backtracking)
Question:Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order."""

#CODE
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        #base case
        if (len(nums)==1):
            return [nums[:]]
        for i in range (len(nums)):
            n=nums.pop(0)
            per =self.permute(nums)
            for perm in per:
                perm.append(n)
            result.extend(per)
            nums.append(n)
#Video solution link:https://www.youtube.com/watch?v=s7AvT7cGdSo
        
        
        return result