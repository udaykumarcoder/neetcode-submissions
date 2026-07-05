class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res=[]
        # left=0
        # right=k-1
        # while(right<len(nums)):
        #     maxim=-10001
        #     templist=nums[left:right+1]
        #     for i in templist:
        #         if(i>maxim):
        #             maxim=i
        #     res.append(maxim)
        #     right=right+1
        #     left=left+1
        # return 
        n = len(nums)

        if n == 0:
            return []

        if k == 1:
            return nums

        left = [0] * n
        right = [0] * n

        # Build left array
        # left[i] = maximum from the start of the block to i
        for i in range(n):
            if i % k == 0:              # Start of a new block
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

        # Build right array
        # right[i] = maximum from i to the end of the block
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:   # End of a block
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        res = []

        # Find maximum for every window
        for i in range(n - k + 1):
            res.append(max(right[i], left[i + k - 1]))

        return res

