# if someone take a leave on someday, he may not be aranged on that work class
def read_leave(c):
    #c example:
    # 17 means (workclass1 on Sunday)
    # 25 means (workclass5 on Friday)
    a,b=divmod(c,10)
    return [a,b]#return the (workclass, day)

#Main Program
# Unicode string
from collections import Counter
from random import sample, choice
import numpy as np
import csv
import os
import sys
#-----------------
max_loop=100
#-----------------
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
        #save the all data in the ac list
        for i,row in enumerate(rows):
            ac.append(row)
        member=ac[0]
        morning=ac[1]
        afternoon=ac[2]
        #Collect the infomation that people who take a leave on someday
        for k in range(3,i+1):
            for p,num in enumerate(ac[k]):
                if (num!=""):
                    sss=read_leave(int(num))
                    sss.append(p)
                    #sss=[member.No, workclass, day]
                    leave1.append(sss)
#workdays list
week=["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
day_num=len(week) #(number of workdays)
for i in range(1,len(member)):
    if (int(morning[i])==1):
        #people who has duty on the workclass1
        morning_p.append(member[i])
    if (int(afternoon[i])==1):
        #people who has duty on the workclass2
        afternoon_p.append(member[i])

#Generate the schedule in random way and give it a score.
#We hope to find a schedule which has score 100.
#Initial the highest score and schedule:
score_max=0
morning_h=[]
afternoon_h=[]
for j in range(max_loop):
    # Random Process
    morning=[choice(morning_p) for i in range(0,day_num)]
    afternoon= [choice(afternoon_p) for i in range(0,day_num)]
    combine=[week,morning,afternoon]
    #score the result
    score=100
    #Person can not shift work whole day
    for i in range(day_num):
        if (morning[i]==afternoon[i]):
            score = score -2
    #the person can not work over 4 times (include 4) in a week
    new_list=morning+afternoon
    #collect how many times people shift work
    c=Counter(new_list).most_common()
    for i in range(len(c)):
        if(c[i][1]>3):
            score = score -2

    #Consider taking a leave
    for info in leave1:
        if (combine[info[0]][info[1]-1]==member[info[2]]):
            #combine[class][weekday-1 to be the list position]
            #print(member[info[2]])
            #print(combine[1])
            #print(combine[2])
            score = score -2
    if(score==100):
        print("j=",j)
        #print(morning)
        #print(afternoon)
        break
    if (score>score_max):
        morning_h=morning
        afternoon_h=afternoon
        score_max=score
if (score!=100):
#   sys.exit("No perfect schdule")
    morning=morning_h
    afternoon=afternoon_h
    print("Highest score = ",score_max)
with open('w_schedule_out.csv','w', newline='') as csvfile1:
    writer=csv.writer(csvfile1)
    writer.writerow(week)
    writer.writerow(morning)
    writer.writerow(afternoon)
    
