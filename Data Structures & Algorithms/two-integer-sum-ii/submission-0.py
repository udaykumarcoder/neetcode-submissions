class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=1
        res=[]
        while(i<len(numbers)):
            for j in range(len(numbers)):
                if(numbers[i]+numbers[j]==target):
                    res.append(i+1)
                    res.append(j+1)
                    return res
                j=j+1
            i=i+1
        return res