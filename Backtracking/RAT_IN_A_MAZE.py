#General information -- (0,0)this co-ordinate is having rat on it and (n-1,n-1)this co-ordinate have cheeze on it.
#we can only move (i+1,j),(i,j+1)
#[[1,0,1]
# [1,1,0]
# [0,1,1]]


def solve(N):
    given_matrix=[]
    solution_matrix=[]
    for i in range(N):
        a=input().split()
        given_matrix+=[list(a)]
    for i in range(N):
        a=[]
        for j in range(N):
            a+=[0]
        solution_matrix+=[a]    
    if solve_matrix(0,0,N,given_matrix,solution_matrix):
        print(solution_matrix)
        return True
    else:
        return False    


def isSafe(i,j,N,given_matrix,solution_matrix):
    return (i<N and j<N and given_matrix[i][j]=='1')

def solve_matrix(i,j,N,given_matrix,solution_matrix):
    if i==N-1 and j==N-1:
        solution_matrix[i][j]=1
        return True

    else:
        if isSafe(i,j,N,given_matrix,solution_matrix):    
            solution_matrix[i][j]=1
            if solve_matrix(i+1,j,N,given_matrix,solution_matrix):
                return True
            elif solve_matrix(i,j+1,N,given_matrix,solution_matrix):
                return True
            else:
                solution_matrix[i][j]=0

        else:
            return False                


solve(5) 


