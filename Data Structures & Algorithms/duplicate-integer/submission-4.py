class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)-1
        ):
            if(nums[i]==nums[i+1]):
                return True
        return False
        # num=set()
        # for i in nums:
        #     if i in num:
        #         return True
        #     num.add(i)
        # return False