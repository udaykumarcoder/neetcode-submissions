class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        res=strs[0]

        for i in range(1,len(strs)):
            word=strs[i]
            temp=""
            p=0
            while(p<min(len(res),len(word))):
                if res[p]==word[p]:
                    temp+=res[p]
                else:
                    break
                p+=1
            res=temp



        return res

        