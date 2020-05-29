#---------------
def solve(N):
    board=[]
    solution=[]
    for i in range(N):
        a=input().split()
        board+=[[int(i) for i in a]]
        b=[]
        for j in range(len(a)):
            b+=[0]
        solution+=[b]    
    
    if solve_rat(board,0,0,N,solution):
        print(solution)
        return True
    else:
        print(-1)
        return False

def solve_rat(board,i,j,N,solution):
    if i==N-1 and j==N-1:
        solution[i][j]=1
        return True
    else:
        if isSafe(board,i,j,N):
            n=board[i][j]
            solution[i][j]=1
            for a in range(1,n+1):
                if solve_rat(board,i+a,j,N,solution):
                    return True
                elif solve_rat(board,i,j+a,N,solution):
                    return True
            solution[i][j]=0
            return False


        else:
            return False                


def isSafe(board,i,j,N):
    return i<N and j<N and board[i][j]>0



solve(5)                      