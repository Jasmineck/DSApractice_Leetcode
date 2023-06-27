"""Link-https://leetcode.com/problems/add-binary/
Solution Link : https://youtu.be/keuWJ47xG8g
WRONG ANSWER COULDN'T SOLVE
Given two binary strings a and b, return their sum as a binary string."""

##CODE--
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        i=0
        arr=[]
        while i<len(a) or i<len(b) or carry==1:
            if a[i]==b[i]:
                if a[i]==1:
                    carry=1
                    arr.append("0")
                else:
                    arr.append("0")
                    carry=0
            else:
                if carry==1:
                    arr.append("0")
                    carry=1
                else:
                    arr.append("1")
                    carry=0
                
        return arr
                
