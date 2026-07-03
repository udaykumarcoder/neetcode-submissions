class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        numscpy=nums.copy()
        for i in numscpy.copy():
            numscpy.remove(i)
            temp=1
            for i in numscpy:
                temp=temp*i
            res.append(temp)
            numscpy=nums.copy()
        return res