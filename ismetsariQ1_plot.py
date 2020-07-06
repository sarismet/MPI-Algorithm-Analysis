import matplotlib.pyplot as plt

import math


Reading_Question1_a = open("Question1_a.txt", "r")
Reading_Question1_b = open("Question1_b.txt", "r")
Reading_Question1_c = open("Question1_c.txt", "r")


a_Lines=Reading_Question1_a.readlines()
b_Lines=Reading_Question1_b.readlines()
c_Lines=Reading_Question1_c.readlines()

general_sizes=[]
general_sequential_values=[]
a_paralel_values=[]


for line in a_Lines:
    line_array=line.strip().split()
    general_sizes.append(int(math.sqrt(int(line_array[0]))))
    general_sequential_values.append(int(line_array[1])/100)
    a_paralel_values.append(int(line_array[2])/100)


b_paralel_values=[]
for line in b_Lines:
    line_array=line.strip().split()
    b_paralel_values.append(int(line_array[2])/100)

c_paralel_values=[]
for line in c_Lines:
    line_array=line.strip().split()
    c_paralel_values.append(int(line_array[2])/100)


plt.figure(1)
plt.plot(general_sizes, general_sequential_values, 'rs')

plt.figure(2)
plt.plot(general_sizes, a_paralel_values, 'bs')

plt.figure(3)

plt.plot(general_sizes, b_paralel_values, 'bs')


plt.figure(4)

plt.plot(general_sizes, c_paralel_values, 'bs')


plt.figure(5)
plt.plot(general_sizes, general_sequential_values, 'rs')
plt.plot(general_sizes, a_paralel_values, 'bs')

plt.figure(6)
plt.plot(general_sizes, general_sequential_values, 'rs')
plt.plot(general_sizes, b_paralel_values, 'bs')

plt.figure(7)
plt.plot(general_sizes, general_sequential_values, 'rs')
plt.plot(general_sizes, c_paralel_values, 'bs')


plt.show()