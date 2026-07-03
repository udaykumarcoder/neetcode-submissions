class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        i=0
        j=1
        ss=set()
        ss.add(s[i])
        count=1
        while(j<len(s)):
            if s[j] not in ss:
                ss.add(s[j])
            else:
                while(s[i]!=s[j]):
                    ss.remove(s[i])
                    i=i+1
                ss.remove(s[i])
                i+=1
                ss.add(s[j])
            count=max(count,j-i+1)
            j=j+1
        return count