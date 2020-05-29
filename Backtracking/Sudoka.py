#---- we are given a board (n*n) and it is given by many numbers and given empty spaces between them....
def solve_sudoku(board,N):
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                break

    if i==N and j==N:
        return True

    for n in range(1,N+1):
        if isSafe(i,j,n,N,board):
            board[i][j]=1
            if solve_sudoku(board,N):
                return True 
            board[i][j]=0


    return False                           

def isSafe(i,j,n,N,board):
    for k in range(N):
        if board[i][k]==n or board[k][j]==n:
            return False                   


    s=int(N**(1/2))
    s_i=i-(i%s)
    s_j=j-(j%s)

    for a in range(s_i,s+1):
        for b in range(s_j,s+1):
            if board[a][b]==n:
                return False

    return True                    


board=[[1,0,3,0],[0,0,2,1],[0,1,0,2],[2,4,0,0]]                                     

solve_sudoku(board,2)

