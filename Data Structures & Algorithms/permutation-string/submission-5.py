class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)):
            return False
        freq1={}
        for i in range(len(s1)):
            freq1[s1[i]]=freq1.get(s1[i],0)+1
        freq2={}
        left=0
        right=len(s1)
        for i in range(left,right):
            freq2[s2[i]]=freq2.get(s2[i],0)+1
        while(right<=len(s2)):
            if(freq1==freq2):
                return True
            if(right==len(s2)):
                return False
            freq2[s2[left]]-=1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            freq2[s2[right]]=freq2.get(s2[right],0)+1
            left=left+1
            right=right+1

        return False
