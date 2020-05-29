#--here we are given a square board(n*n) and we have to place n queens on the board such that no two queens can attack each other.

def solve(N):
    if N>=4:
        solve_board=[]
        for i in range(N):
            a=[]
            for j in range(N):
                a+=[0]
            solve_board+=[a]    
        if solve_queen(0,N,solve_board):
            print(solve_board)
            return True
    else:
        print("Please enter number >=4!") 
        return False

def solve_queen(col,N,solve_board):
    if col==N:
        return True
    else:
        for i in range(N):
            if isSafe(i,col,N,solve_board):
                solve_board[i][col]=1
                if solve_queen(col+1,N,solve_board):
                    return True
                solve_board[i][col]=0
        return False

def isSafe(row,col,N,solve_board):
    for i in range(col):
        if solve_board[row][i]:
            return False
    j=col
    for i in range(row,N):
        if j>=0:
            if solve_board[i][j]:
                return False
            j-=1
        else:
            break

    j=col
    for i in range(row,-1,-1):
        if j>=0:
            if solve_board[i][j]:
                return False
            j-=1
        else:
            break
    return True        


solve(25)    