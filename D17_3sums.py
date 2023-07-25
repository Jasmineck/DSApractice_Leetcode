#code-- 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        s = set()
        op=[]
        
        
        for i in range (l):
            if i<l-1:
                for j in range(i+1,l):
                    sums=nums[i]+nums[j]
                    sums=-sums
                    print(sums)
                    if (nums[i],nums[j],sums) not in s:
                        if sums in nums[i+2::] and sums!=nums[i] and nums[j]  :
                        
                            s.add((nums[i],nums[j],sums))
        op=list(s)
        return op
                