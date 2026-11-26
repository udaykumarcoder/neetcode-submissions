class UnionFind:
    def __init__(self,n):
        self.n=n
        self.par=list(range(n+1))
        self.size=[1]*n

    def find(self,node):
        while self.par[node]!=node:
            self.par[node]=self.par[self.par[node]]
            node=self.par[node]
        return node
    
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return False
        self.n-=1
        if self.size[pu]>=self.size[pv]:
            self.size[pu]+=self.size[pv]
            self.par[pv]=pu
        else:
            self.size[pv]+=self.size[pu]
            self.par[pu]=pv
        return True
    
    def isconnected(self):
        return self.n==1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf=UnionFind(len(nums))
        factor_index={}
        for i,n in enumerate(nums):
            f=2
            while f*f<=n:
                if n%f==0:
                    if f in factor_index:
                        uf.union(i,factor_index[f])
                    else:
                        factor_index[f]=i
                    while n%f==0:
                        n=n//f
                f+=1
            if n>1:
                if n in factor_index:
                    uf.union(i,factor_index[n])
                else:
                    factor_index[n]=i
        return uf.isconnected()