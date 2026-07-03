class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxim=0
        # i=0
        # while(i<len(heights)):
        #     j=i+1
        #     while(j<len(heights)):
        #         b=j-i
        #         l=min(heights[i],heights[j])
        #         temp=l*b
        #         maxim=max(temp,maxim)
        #         j=j+1
        #     i=i+1
        # return maxim
        i=0
        maxim=0
        j=len(heights)-1
        while(i<j):
            l=min(heights[i],heights[j])
            b=j-i
            temp=l*b
            maxim=max(temp,maxim)
            if(heights[i]<heights[j]):
                i=i+1
            else:
                j=j-1
        return maxim



