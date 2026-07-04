class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case if s2 len is small return false
        freq1={}
        for i in range(len(s1)):
            freq1[s1[i]]=freq1.get(s1[i],0)+1
        freq2={}
        left=0
        right=len(s1)
        while(right<=len(s2)):
            for i in range(left,right):
                freq2[s2[i]]=freq2.get(s2[i],0)+1
            if(freq1==freq2):
                return True
            freq2={}
            left=left+1
            right=right+1
        return False
