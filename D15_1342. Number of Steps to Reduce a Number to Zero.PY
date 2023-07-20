"""Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
SOLVED
Q-Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 """
 class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num>0:
            count=count+1
            if num%2==0:
                num=num//2
            else:
                num=num-1
        return count
        