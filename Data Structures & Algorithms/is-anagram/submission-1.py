class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        l1=[char for char in s]
        l1.sort()
        l2=[char for char in t]
        l2.sort()
        result=True if l1==l2 else False
        return result

        
        





