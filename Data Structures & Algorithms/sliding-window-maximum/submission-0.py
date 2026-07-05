class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        left=0
        right=k-1
        while(right<len(nums)):
            maxim=-10001
            templist=nums[left:right+1]
            for i in templist:
                if(i>maxim):
                    maxim=i
            res.append(maxim)
            right=right+1
            left=left+1
        return res

