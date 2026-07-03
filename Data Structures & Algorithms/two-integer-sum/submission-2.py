class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        j=1
        for i in range(0,len(nums)-1):
            j=i+1
            while(j<=len(nums)-1):
                if(nums[i]+nums[j]==target):
                    res.append(i)
                    res.append(j)
                    return res
                j=j+1
        return res

            

