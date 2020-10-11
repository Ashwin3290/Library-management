from library_database import *
from datetime import datetime, timezone
import random
print('		               WELCOME TO LIBRARY MANAGER')
print('YOU CAN DO THE FOLLOWING OPERATIONS:')
print('1:ADD A MEMBER\n2:BOOK ISSUE\n3:BOOK RETURN\n4:SHOW ISSUE HISTORY OF A BOOK\n5:DELETE DATA OF A MEMBER\n6:EXIT')
def slicer(t):
    x=''
    for i in range(0,16):
        x+=t[i]
    return x
r=True
while r:
        print('ENTER YOUR CHOICE; ')
        m=input()
        if m=='1':
            try:
                a=''
                b=0
                c=0
                for g in range(3):
                    if g==0:
                        a=input('ENTER NAME OF APPLICANT') 
                    if g==1:
                        b=int(input('ENTER PHONE NUMBER OF APPLICANT '))
                    if g==2:
                        c=random.randint(1,100000000)
                print('THE UNIQUE MEMBERSHIP NUMBER GENERATED IS ',c)
                minsert(a,b,c)
            except:
                print('ERROR IN QUERY TRY AGAIN')
        
            
        elif m=='2' :
            try:
                a=''
                d=''
                b=0
                c=''
                
                for i in range(4): 
                    if i==0:
                        a=int(input('ENTER MEMBERSHIP NUMBER;  '))
                    if i==1:
                        d=input('ENTER BOOK NAME:  ')
                    if i==2:
                        b=int(input('ENTER BOOK SERIAL NUMBER ;  '))
                    if i==3:
                        utc_dt = datetime.now(timezone.utc)#gmt time
                        mn= utc_dt.astimezone() # local time
                        c=slicer(str(mn))
                insert(a,d,b,c)
            except:
                print('ERROR IN QUERY TRY AGAIN')
            
        elif m=='3' :
            try:
                print('ENTER THE SERAL NUMBER OF THE BOOK')
                z=int(input())
                utc_dt = datetime.now(timezone.utc)#gmt time
                te= utc_dt.astimezone() # local time
                x=slicer(str(te))
                update(z,x)
            except:
                print('ERROR IN QUERY TRY AGAIN')
        elif m=='4':
            try:
                print('YOU CAN SEE THE ISSUE HISTORY OF A BOOK BY ENTERING ITS SERIAL NUMBER')
                s= int(input())
                show(s)
            except:
                print('ERROR IN QUERY TRY AGAIN')
                
        elif m=='5':
            try:
                print('ENTER MEMBERSHIP NUMBER OF THE PERSON WHOSE RECORD HAS TO BE DELETED')
                c=int(input())
                delete(c)
            except:
                print('ERROR IN QUERY TRY AGAIN')
        elif m=='6':
            quit()
        
