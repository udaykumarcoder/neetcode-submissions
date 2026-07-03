class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        mapping={}
        for i in range(0,len(strs)):
            temp=list(strs[i])
            temp.sort()
            tempstr="".join(temp)
            if tempstr in mapping:
                mapping[tempstr].append(strs[i])
            else:
                mapping[tempstr]=[strs[i]]
        res=(list(mapping.values()))
        return res