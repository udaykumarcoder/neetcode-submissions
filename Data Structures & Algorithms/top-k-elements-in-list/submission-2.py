class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        kfreq=sorted(count.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            res.append(kfreq[i][0])
        return res