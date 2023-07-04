"""Link:
HALF SOLVED 
Q:Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= nums1 < nums2 <= right .
nums1 and nums2 are both prime numbers.
nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself."""

#------CODE-------
import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #sieven algorithm to get all primt within the range
        arr = [1 for i in range(right+1)] 
        arr[0]=0
        arr[1]=0
        sq=floor(math.sqrt(right))
        for i in range(2,sq+1):
            if arr[i]==1:
                for j in range(2*i,right,i):
                    arr[j]=0
        arr=arr[left:right+1] #getting array between the range