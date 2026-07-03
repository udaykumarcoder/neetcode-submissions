class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxim=0
        i=0
        while(i<len(heights)):
            j=i+1
            while(j<len(heights)):
                b=j-i
                l=min(heights[i],heights[j])
                temp=l*b
                maxim=max(temp,maxim)
                j=j+1
            i=i+1
        return maxim


