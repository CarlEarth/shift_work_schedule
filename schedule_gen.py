def read_leave(c):
    a,b=divmod(c,10)
    return [a,b]#return the (class, day)

# Unicode string
from collections import Counter
from random import sample, choice
import numpy as np
import csv
import os
import sys
morning=[]
afternoon=[]
morning_p=[]
afternoon_p=[]
leave1,leave2=[],[]
ac=[]
checkname='w_schedule_in.csv'
if os.path.isfile(checkname):
    print("test")
    with open(checkname, newline='') as csvfile:
        rows = csv.reader(csvfile)
        #save the data in the ac
        for i,row in enumerate(rows):
            ac.append(row)
        member=ac[0]
        morning=ac[1]
        afternoon=ac[2]
        #Collect the people who take a leave on some time
        for k in range(3,i+1):
            for p,num in enumerate(ac[k]):
                if (num!=""):
                    sss=read_leave(int(num))
                    sss.append(p)
                    leave1.append(sss)
        print(leave1)
#class man(self,num1,num2,no1,no2):
#morning_p=["Mary","Rose","Carl","Alice"]
#afternoon_p=["Andy","Paul","Carl","Alice"]
week=["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(1,len(member)):
    if (int(morning[i])==1):
        morning_p.append(member[i])
    if (int(afternoon[i])==1):
        afternoon_p.append(member[i])

#Preprocess the input data
#del morning_p[0]
#del afternoon_p[0]
for j in range(10):
    day_num=len(week)
    morning=[choice(morning_p) for i in range(0,day_num)]
    afternoon= [choice(afternoon_p) for i in range(0,day_num)]
    combine=[week,morning,afternoon]
    #score the result
    score=100
    #the person can not shift work whole day
    for i in range(day_num):
        if (morning[i]==afternoon[i]):
            score = score -2
    #the person can not work over 4 times (include 4) 
    new_list=morning+afternoon
    c=Counter(new_list).most_common()
    #print(c)
    for i in range(len(c)):
        if(c[i][1]>3):
            score = score -2
	#print(c[i][1])
    #print(score)
    #Consider the leave of a day
    for info in leave1:
        if (combine[info[0]][info[1]-1]==member[info[2]]):
            #combine[class][weekday-1 to be the list position]
            print(member[info[2]])
            print(combine[1])
            print(combine[2])
            score = score -2
    if(score==100):
        print("j=",j)
        #print(morning)
        #print(afternoon)
        break
if (score!=100):
    sys.exit("No perfect schdule")

with open('w_schedule_out.csv','w', newline='') as csvfile1:
    writer=csv.writer(csvfile1)
    writer.writerow(week)
    writer.writerow(morning)
    writer.writerow(afternoon)
    
