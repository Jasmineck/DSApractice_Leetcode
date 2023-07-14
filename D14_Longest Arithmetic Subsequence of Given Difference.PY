"""lINK:https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

Q:Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

"""
#CODE:

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count=0
        difference=abs(difference)
        for x in range (len(arr)-1):
            if x==0 and arr[0]-0==difference:
                    count=count+1
            if abs(arr[x+1]-arr[x])==difference:
                count=count+1
        return count
            