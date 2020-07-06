import numpy as np
import random

size_array = []

for i in range(1, 21):
    size_array.append(i*i)

time = 0
outputList_a = []
outputList_b = []
outputList_c = []
str_sequential = []
str_parallel_a = []
str_parallel_b = []
str_parallel_c = []
while time < 20:
    N = size_array[time]

    X = np.zeros([N, N], dtype=int)

    Y = np.copy(X)

    result = np.copy(X)

    for a in range(N):
        for b in range(N):
            X[a][b] = random.randint(0, 10*N)
            Y[a][b] = random.randint(0, 10*N)

    sequential_count = 0
    parallel_count = 0

    # iterate through rows of X
    for i in range(N):
        # iterate through columns of Y
        for j in range(N):
            # iterate through rows of Y
            parallel_count = parallel_count+1
            for k in range(N):
                sequential_count = sequential_count+1
                result[i][j] += X[i][k] * Y[k][j]
    str_sequential.append(sequential_count)
    str_parallel_a.append(parallel_count)
    the_string_to_write_on_file = str(
        N)+" "+str(sequential_count)+" "+str(parallel_count)
    outputList_a.append(the_string_to_write_on_file)
    parallel_count = 0
    result = np.zeros([N, N], dtype=int)
    for i in range(N):
        # iterate through columns of Y
        for j in range(N):
            # iterate through rows of Y
            parallel_count = parallel_count+1
            for k in range(N):
                result[i][(j + k) % N] += X[i][k] * Y[k][(j + k) % N]
    str_parallel_b.append(parallel_count)
    the_string_to_write_on_file = str(
        N)+" "+str(sequential_count)+" "+str(parallel_count)
    outputList_b.append(the_string_to_write_on_file)


    parallel_count = 0
    result = np.zeros([N, N], dtype=int)

    for a in range(N):
        operation_no = 1+(N-1)*a
        parallel_count = parallel_count+operation_no
        X[a] = np.roll(X[a], -a)

    for b in range(N):
        operation_no = 1+(N-1)*b
        parallel_count = parallel_count+operation_no
        Y[:, b] = np.roll(Y[:, b], -b, axis=0)

    for k in range(N):
        for i in range(N):
            for j in range(N):

                result[i][j] += X[i][j] * Y[i][j]

        for a in range(N):
            parallel_count = parallel_count+(N-1)+1
            X[a] = np.roll(X[a], -1)
        for b in range(N):
            parallel_count = parallel_count+(N-1)+1
            Y[:, b] = np.roll(Y[:, b], -1, axis=0)

    str_parallel_c.append(parallel_count)
    the_string_to_write_on_file = str(
        N)+" "+str(sequential_count)+" "+str(parallel_count)
    print
    outputList_c.append(the_string_to_write_on_file)

    time = time + 1

WritingOnOutFile_a = open("Question1_a.txt", "w")
WritingOnOutFile_a.write('\n'.join(outputList_a))
WritingOnOutFile_a.close()

WritingOnOutFile_b = open("Question1_b.txt", "w")
WritingOnOutFile_b.write('\n'.join(outputList_b))
WritingOnOutFile_b.close()

WritingOnOutFile_c = open("Question1_c.txt", "w")
WritingOnOutFile_c.write('\n'.join(outputList_c))
WritingOnOutFile_c.close()

print("Algorithm Type, Input Size = 1,Input Size = 2,Input Size = 3,Input Size = 4,Input Size = 5,Input Size = 6,Input Size = 7,Input Size = 8,Input Size = 9,Input Size = 10,Input Size = 11")
print("Sequential Algorithm,", end="")



for k,item in enumerate(str_sequential):
    if k != len(str_sequential)-1:
        print(item, end=",")
    else:
        print(item)

print("CRCW Algorithm,", end="")

for k,item in enumerate(str_parallel_a):
    if k != len(str_parallel_a)-1:
        print(item, end=",")
    else:
        print(item)

print("EREW Algorithm,", end="")

for k,item in enumerate(str_parallel_b):
    if k != len(str_parallel_b)-1:
        print(item, end=",")
    else:
        print(item)

print("2-D Meshes Algorithm,", end="")

for k,item in enumerate(str_parallel_c):
    if k != len(str_parallel_c)-1:
        print(item, end=",")
    else:
        print(item)
