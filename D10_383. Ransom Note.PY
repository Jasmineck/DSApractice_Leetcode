"""Link:https://leetcode.com/problems/ransom-note/
SOLVED
Q: Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""

#-----CODE------
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine=list(magazine)
        for x in ransomNote:
            if x in magazine:
                magazine.remove(x)
            else:
                return False
        return True
            

 