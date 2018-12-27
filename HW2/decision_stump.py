import random as rd
import operator
import csv


DATASIZE = 20


data = []

class point(object):
    def __init__(self, x=0.0, y=0):
        self.x = (float)(x)
        self.y = (int)(y)

class hypothesis(object):
    def __init__(self, s=0, theta=0.0):
        self.s = s
        self.theta = theta

def sign(x):
    if( x<=0 ):
        return -1
    else:
        return 1

def make_noise():
    for i in range(0, len(data)):
        rnum = rd.randint(1,10)
        if( rnum<=2 ):
            data[i].y *= -1

def make_data():
    for i in range(0, DATASIZE):
        rnum =  rd.random()*2 - 1 
        tmp = point()
        tmp.x = rnum
        tmp.y = sign(tmp.x)
        data.append(tmp)

def check(temp):
    error = 0
    for now in data:
        if now.y != temp.s * sign(now.x - temp.theta):
            error+=1
    return error/float(len(data))

def calculate():
    global minrate
    re = hypothesis()
    temp = hypothesis()
    minErrorRate = 1.0
    # s=1 枚舉所有theta
    for i in range(0, len(data)+1):
        temp.s = 1
        if i == 0:
            #最左邊
            temp.theta = -2.0
        elif i == len(data):
            #最右邊
            temp.theta = 1.0
        else:
            #其他
            temp.theta = (data[i].x + data[i-1].x)/2

        tmpErrorRate = check(temp)
        if( tmpErrorRate < minErrorRate ):
            minErrorRate = tmpErrorRate
            re = hypothesis(temp.s, temp.theta)

    #s=-1
    for i in range(0, len(data)+1):
        temp.s = -1
        if i == 0:
            #最左邊
            temp.theta = -2.0
        elif i == len(data):
            #最右邊
            temp.theta = 1.0
        else:
            #其他
            temp.theta = (data[i].x + data[i-1].x)/2

        tmpErrorRate = check(temp)
        if( tmpErrorRate < minErrorRate ):
            minErrorRate = tmpErrorRate
            re = hypothesis(temp.s, temp.theta)


    minrate = minErrorRate
    return re


def calculate_out(ans):
    return 0.5 + 0.3*float(ans.s) * float(abs(ans.theta)-1.0)

TIMES = 1000
ans = hypothesis()
minrate  =0.0
totalinRate = 0.0
totaloutRate = 0.0


# main
with open("test.csv", "w") as csvfile:
    writer = csv.writer(csvfile)

    for i in range(0, TIMES):
        data.clear()

        make_data()
        make_noise()

        data.sort(key=operator.attrgetter('x'))
        ans.s = 0.0
        ans.theta = 0
        
        # for now in data:
        #     print( now.x, now.y )
        ans = calculate()


        # print(ans.s, ans.theta)
        # print(minrate)
        nowout = calculate_out(ans)
        # print("Ein")
        # print(minrate)
        # print("Eout")
        # print(nowout)
        towrite = minrate - nowout
        lst = [towrite]
        writer.writerow( lst )


        totalinRate += minrate
        totaloutRate += nowout


csvfile.close()

print(totalinRate / TIMES)
print(totaloutRate / TIMES)














