class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for sr in range(0,9,3):
            for sc in range(0,9,3):    
                ans=self.searchSubmatrix(board,sr,sc)
                if(ans==False):
                    return False
        return True

    def searchSubmatrix(self,board:List[List[str]],sr:int,sc:int)->bool:
        count={}
        for i in range(sr,sr+3):
            for j in range(sc,sc+3):
                if board[i][j]=='.':
                    continue
                ans=self.isvalidrook(board,board[i][j],i,j)
                if(ans==False):
                    return False
                count[board[i][j]]=count.get(board[i][j],0)+1
        if any(value>1 for value in count.values()):
            return False
        return True
    
    def isvalidrook(self,board:List[List[str]],boardvalue:str,row:int, col:int)->bool:
        for i in range(0,9):
            if(i!=col and boardvalue==board[row][i]):
                return False
            
            if(i!=row and boardvalue==board[i][col]):
                return False
            
        return True

