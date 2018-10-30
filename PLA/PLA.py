# reference: https://blog.csdn.net/a1015553840/article/details/50979434
import random as rd
import csv

# open data "train.dat" as read mode
# data form input(4D), output(1D):{0,-1}
data = open("train.dat", "r")

# Dimension
global Dimension
Dimension = 5

# counter   
global step

# return the sum of two tuples
def update(a, b):
    c = tuple( round(float(a[i])+float(b[i]), 6) for i in range(0, Dimension) )
    return c

# return sign of a, and take sign(0) as -1
def sign(a):
    if a<=0:
        return -1
    else:
        return 1

# return the inner product of two tuples
def in_pro(a, b):
    r = 0.
    for i in range(0, Dimension):
        r+= float(a[i])*float(b[i])
    return r

# constant multiply
def cmul(c, b):
    r = tuple( round(c*float(b[i]), 6) for i in range(0, Dimension) )
    return r

# Perceptron Learning Algorithm
def PLA(w):
    global step
    cnt = 0
    idx = 0
    complete = 0
    while True:
        if int(lst[idx][Dimension]) == sign( in_pro(w, lst[idx]) ):
            cnt += 1
        else:
            tmp = cmul(float(lst[idx][Dimension]), lst[idx])
            w = update(w, tmp)
            step += 1
            cnt = 0
        if idx == len(lst)-1:
            idx = 0
        else:
            idx += 1
        if cnt == len(lst):
            break

#########################################################################################################

# init data list
lst = []

# origin w
w = (0, 0, 0, 0, 0)

# seperate input and put it to tuple list, lst
for line in data:
    lst.append( tuple( [1] + list(i for i in line.split()) ) )

# run PLA 1126 times!!
TIMES = 1126

timer = TIMES
sum = 0
ans = []

# build the csv file to store the outcome
with open('output2.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')    
    while timer:
        # random shuffle
        rd.shuffle(lst)

        #initial step
        step = 0
        PLA(w)
        ans = str(step)
        sum += step
        timer -= 1
        writer.writerow( i for i in ans )

print(sum/TIMES)

   