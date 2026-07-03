class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        se=set(nums)
        if(len(nums)==0):
            return res
        i=len(nums)-1
        while(i>=0):
            ans=target-nums[i]
            if ans in se:
                res.append(nums.index(ans))
                res.append(i)
                return res
            i=i-1
        return res
        # j=1
        # for i in range(0,len(nums)-1):
        #     j=i+1
        #     while(j<=len(nums)-1):
        #         if(nums[i]+nums[j]==target):
        #             res.append(i)
        #             res.append(j)
        #             return res
        #         j=j+1
        # return res

            

