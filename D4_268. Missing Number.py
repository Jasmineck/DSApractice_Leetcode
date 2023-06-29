"""Link: https://leetcode.com/problems/missing-number/
SOLVED- Q- Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=0
        for i in range ( len(nums)):
            if nums[i]!=i:
                n=i
                break
            if i==len(nums)-1:
                n=i+1
        return n