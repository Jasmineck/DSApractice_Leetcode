"""Link: https://leetcode.com/problems/plus-one/
HALF SOLVED
OUTPUT IS COMING IN WEIRD ORDER
Q:You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""

#-----CODE------
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        arr=1
        if digits[l-1]<9:
            digits[l-1]=1+ digits[l-1]
        else:
            for x in range(l-1,l):
                if x==0:
                    digits[0]=1
                    digits.insert(1,0)
                    

                    break
                    
                if digits[x]==9 :
                    digits[x]=0
                    digits[x-1]=1+digits[x-1]
        return digits