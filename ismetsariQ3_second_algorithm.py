import numpy as np
import random
import time
import matplotlib.pyplot as plt
N = 8
board=None
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


def QueensLasVegas_similar(columns,k):

    AvailColumns = []
    for i in range(N):
        AvailColumns.append(i)

    R = 0
    i=0
    while len(AvailColumns) != 0 and R <= N - 1 and i<k:

        index = random.randint(0,len(AvailColumns)-1)

        C=AvailColumns[index]
        columns[R] = C
        board[R][C] = 1
        R = R + 1
        if R!=N:
            AvailColumns = updateColumns(R)
        i=i+1

def QueensLasVegas(columns):
    
    AvailColumns = []
    for i in range(N):
        AvailColumns.append(i)

    R = 0
    i=0
    while len(AvailColumns) != 0 and R <= N - 1:

        index = random.randint(0,len(AvailColumns)-1)

        C=AvailColumns[index]
        columns[R] = C
        board[R][C] = 1
        R = R + 1
        if R!=N:
            AvailColumns = updateColumns(R)
        i=i+1

def N_queen(n,limit):
    if n==0:
        return True
    for i in range(limit,N):
        for j in range(0,N):
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queen(n-1,limit)==True:
                    return True
                board[i][j] = 0

    return False
def determine_starting_point_of_backtracking(columns):
    #print("columns are : ",columns)
    for count,c in enumerate(columns):
        if c ==-1:
            return count



def normal(normal_times):
    total=0
    global board
    for i in range(1000):
        
        board = np.zeros([N, N], dtype = int) 

        columns = [-1,-1,-1,-1,-1,-1,-1,-1]
        start_time = time.time()
        QueensLasVegas(columns)
        normal_times.append(time.time() - start_time)
        if sum(columns)==28:
            total+=1


    print("normal ",total/1000)

def similar(similar_times,similar_dict,success,similar_execution_times):
    total=0
    global board
    
    for i in range(1000):
        board = np.zeros([N, N], dtype = int) 

        columns = [-1,-1,-1,-1,-1,-1,-1,-1]
        k=random.randint(0,7)

        success[k]=success[k]+1

        start_time = time.time()
        QueensLasVegas_similar(columns,k)

        starting_point=determine_starting_point_of_backtracking(columns)
        
        if N_queen((8-starting_point),starting_point):
            r=similar_dict.get(k,-1)
            s=similar_dict.get(k)+1
            similar_dict.update({k:s})
            total+=1
        t_now=time.time() - start_time
        similar_times.append(t_now)

        p_time=similar_execution_times.get(k)
        similar_execution_times.update({k:p_time+t_now})
    print("similar ",total/1000)
def split_word(s):
    n=8
    return '-\n'.join(s[i:i+n] for i in range(0, len(s), n))
normal_times=[]
similar_times=[]
similar_dict={}
similar_execution_times={}
for i in range(8):
    similar_dict.update({i:0})
    similar_execution_times.update({i:0})
similar_dict_success={}
success=[0,0,0,0,0,0,0,0]
normal(normal_times)

similar_execution_times_distribution={}
similar(similar_times,similar_dict,success,similar_execution_times)

similar_dist=[]

for count,s in enumerate(success):
    value=similar_dict[count]
    value2=similar_execution_times[count]

    if value!=0:
        similar_dict_success.update({count:value/s})
        similar_execution_times_distribution.update({count:float(value2/s)})
    
    if s!=0:
        similar_dist.append(float(value2/s))

    elif s==0:
        similar_dist.append(float(0))
Dictionary_Length = len(similar_dict)
for key in similar_dict_success:
    print("key is",key," and success is : ",similar_dict_success[key])

times=[x for x in range(1,1001)]

plt.figure(1)
plt.plot(times, normal_times, 'rs')
plt.plot(times, similar_times, 'bs')

plt.figure(2)
plt.bar(range(len(similar_dict)), similar_dict.values(), align="center")
plt.xticks(range(len(similar_dict)), list(similar_dict.keys()))

plt.figure(3)
plt.bar(range(len(similar_dict_success)), similar_dict_success.values(), align="center")
plt.xticks(range(len(similar_dict_success)), list(similar_dict_success.keys()))

plt.figure(4)
plt.subplot(1,2,1)
plt.plot(times, normal_times, 'rs')
plt.subplot(1,2,2)
plt.plot(times, similar_times, 'bs')


ks=[x for x in range(8)]

plt.figure(5)
plt.subplot(1,2,1)
plt.bar(range(len(similar_execution_times_distribution)), similar_execution_times_distribution.values(), align="center")
plt.xticks(range(len(similar_execution_times_distribution)), list(similar_execution_times_distribution.keys()))
plt.subplot(1,2,2)
plt.plot(ks, similar_dist, 'bs')
plt.show()