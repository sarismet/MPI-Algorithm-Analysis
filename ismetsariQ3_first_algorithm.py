import numpy as np
import random

N = 8
board=None
outputFile=open("executions_phases.txt","w")
def is_attack(i, j):
    #checking if there is a queen in row or column
    try:
        for k in range(0, N):
            if board[i][k] == 1 or board[k][j] == 1:
                return True
        #checking diagonals
        for k in range(0, N):
            for l in range(0, N):
                if (k + l == i + j) or (k - l == i - j):
                    if board[k][l] == 1:
                        return True
        return False
    except:
        print("R is ",i," Coulmn is : ",j)


def updateColumns(R):
    temp = []
    for column in range(0,N):
        if is_attack(R, column) == False:
            temp.append(column)
                

    #print("returned list is , ",list(set(temp)))
    return list(set(temp))


def QueensLasVegas(columns):

    AvailColumns = []
    for i in range(N):
        AvailColumns.append(i)

    R = 0
    i=0
    string_to_write=""
    while len(AvailColumns) != 0 and R <= N - 1:
        string_to_write="R is "+str(R)+" and available are ["
        for cs in AvailColumns:
            string_to_write=string_to_write+str(cs)+","

        string_to_write=string_to_write+"]\n"
        outputFile.write(string_to_write)
        index = random.randint(0,len(AvailColumns)-1)
        
        outputFile.write("The index selected randomly is"+str(index)+"\n")
        C=AvailColumns[index]
        string_to_write="The chosen column from available lists is : "+str(C)+"\n"
        outputFile.write(string_to_write)
        outputFile.write("Inserting the current queen to chosen column ... \n")
        columns[R] = C
        board[R][C] = 1
        outputFile.write("After inserting the board looks like ... \n")
        string_to_write=""
        for b in board:
            for b2 in b:
                string_to_write+=str(b2)+" "
            string_to_write+="\n"
        string_to_write+="\n"    
        outputFile.write(string_to_write)
        R = R + 1
        if R!=N:
            outputFile.write("Updating available columns ... \n")
            AvailColumns = updateColumns(R)
            string_to_write="Updated available columns are [ "
            for cs in AvailColumns:
                string_to_write=string_to_write+str(cs)+","
            string_to_write=string_to_write+"]\n"
            outputFile.write(string_to_write)
        i=i+1


for a in range(10):
    total=0
    for i in range(1000):
        board = np.zeros([N, N], dtype = int) 

        columns = [-1,-1,-1,-1,-1,-1,-1,-1]
        outputFile.write("Starting the execution of QueensLasVegas algorithm \n\n")
        QueensLasVegas(columns)

        if sum(columns)==28:
            outputFile.write("We success to place all the Queens!!!!\n\n\n\n")
            total+=1
        else:
            outputFile.write("We fail success to place all the Queens!!!!\n\n\n\n")

    print(total/1000)

outputFile.close()