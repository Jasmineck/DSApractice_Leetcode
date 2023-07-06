"""Link: https://leetcode.com/problems/search-insert-position/
SOLVED WITH BINARY SEARCH
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

#-----CODE------
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=len(nums)
        low=0
        high=l-1
        if target>nums[l-1]:
            return l
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            else:
                if target>nums[mid]:
                    low=mid+1
                else:
                    high= mid-1
        return low