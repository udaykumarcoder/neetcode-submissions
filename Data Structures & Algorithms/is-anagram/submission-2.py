class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        freq={}
        for char in s :
            freq[char]=freq.get(char,0)+1
        for char in t:
            if char not in freq:
                return False
            freq[char]-=1
            if(freq[char]<0):
                return False
        return True
        # l1=[char for char in s]
        # l1.sort()
        # l2=[char for char in t]
        # l2.sort()
        # result=True if l1==l2 else False
        # return result

        
        





