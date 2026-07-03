class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i=0
        # j=1
        # res=[]
        # while(i<len(numbers)):
        #     for j in range(len(numbers)):
        #         if(numbers[i]+numbers[j]==target):
        #             res.append(i+1)
        #             res.append(j+1)
        #             return res
        #         j=j+1
        #     i=i+1
        # return res
        i=0
        res=[]
        j=len(numbers)-1
        while(i<j):
            if(numbers[i]+numbers[j]==target):
                res.append(i+1)
                res.append(j+1)
                return res
            if(numbers[i]+numbers[j]>target):
                j=j-1
            if(numbers[i]+numbers[j]<target):
                i=i+1
        return res