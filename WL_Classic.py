from collections import Counter
from operator import or_
from operator import and_
import functools


#set up variables and find how many node
node_num = int(input())
user1 = []
record1 = ["0", "0"]
keep_going = True
histos1 = []
u1 = []
temp1 = 0
tu1 = []
tc1 = []
tu2 = []
tc2 = []

user2 = []
record2 = ["0", "0"]
histos2 = []
u2 = []
temp2 = 0
color1 = [1]*node_num
color2 = [1]*node_num
#input the matrix
for i in range(0, node_num):
    user1.append(list(map(int, input().split())))

for i in range(0, node_num):
    user2.append(list(map(int, input().split())))


histos1 = color1.copy()
histos2 = color2.copy()
#creating a same size matrix as a backup 

Continue = True #default to repeat loop
    
x=0

while Continue: #change this stop after stability

    tu1.clear() #reset the used array
    tc1.clear()

    search1 = ""
    search2 = ""

    #WL test calculations
    for i in range(0, len(user1)):
        search1 = Counter(map((lambda a: color1[i] * a), user1[i])).most_common()

        search1.sort()
        if str(search1) in record1:
            histos1[i] = record1.index(str(search1)) #convert using numbers
        else:
            histos1[i] = len(record1)
            record1.append(str(search1))
        search2 = Counter(map(lambda a: color2[i] * a, user2[i])).most_common()

        search2.sort()
        if str(search2) in record2:
            histos2[i] = record2.index(str(search2))
        else:
            histos2[i] = len(record2)
            record2.append(str(search2))


    
    
    ctu1 = Counter(color1).most_common()
    ctc1 = Counter(histos1).most_common()
    ctu1.sort()
    ctc1.sort()

    second = lambda c: list(map(lambda z: z[1], c))
    end1 = second(ctc1) == second(ctu1)


        
    ctu2 = Counter(color2).most_common()
    ctc2 = Counter(histos2).most_common()
    ctu2.sort()
    ctc2.sort()

    end2 = second(ctc2) == second(ctu2)
    
    

    Continue = not(end2 or end1)
    


    color1 = histos1.copy()
    color2 = histos2.copy()

    
    

        

    #can compare user and copy 
    x+=1


#use this method up in the check stability 



cu1 = Counter(color1).most_common()
cu2 = Counter(color2).most_common()
cu1.sort()
cu2.sort()



result = True

conclusion1 = []
conclusion2 = []
#extract

if len(cu1) == len(cu2):
    c1 = lambda l: list(map(lambda c: c[1], l)).sort()
    conclusion1 = c1(cu1)
    conclusion2 = c1(cu2)
    if conclusion1 == conclusion2:
        print("We cannot conclude that they are different")
    else:
        print("We can conclude that they are different")
else:
    print("We can conclude that they are different")
#compare and conclusion


from collections import Counter
from operator import or_
from operator import and_
import functools


#set up variables and find how many node
node_num = int(input())
user1 = []
record1 = ["0", "0"]
keep_going = True
histos1 = []
u1 = []
temp1 = 0
tu1 = []
tc1 = []
tu2 = []
tc2 = []

user2 = []
record2 = ["0", "0"]
histos2 = []
u2 = []
temp2 = 0
color1 = [1]*node_num
color2 = [1]*node_num
#input the matrix
for i in range(0, node_num):
    user1.append(list(map(int, input().split())))

for i in range(0, node_num):
    user2.append(list(map(int, input().split())))


histos1 = color1.copy()
histos2 = color2.copy()
#creating a same size matrix as a backup 

Continue = True #default to repeat loop
    
x=0

while Continue: #change this stop after stability

    tu1.clear() #reset the used array
    tc1.clear()

    search1 = ""
    search2 = ""

    #WL test calculations
    for i in range(0, len(user1)):
        search1 = Counter(map((lambda a: color1[i] * a), user1[i])).most_common()

        search1.sort()
        if str(search1) in record1:
            histos1[i] = record1.index(str(search1)) #convert using numbers
        else:
            histos1[i] = len(record1)
            record1.append(str(search1))
        search2 = Counter(map(lambda a: color2[i] * a, user2[i])).most_common()

        search2.sort()
        if str(search2) in record2:
            histos2[i] = record2.index(str(search2))
        else:
            histos2[i] = len(record2)
            record2.append(str(search2))


    
    
    ctu1 = Counter(color1).most_common()
    ctc1 = Counter(histos1).most_common()
    ctu1.sort()
    ctc1.sort()

    second = lambda c: list(map(lambda z: z[1], c))
    end1 = second(ctc1) == second(ctu1)


        
    ctu2 = Counter(color2).most_common()
    ctc2 = Counter(histos2).most_common()
    ctu2.sort()
    ctc2.sort()

    end2 = second(ctc2) == second(ctu2)
    
    

    Continue = not(end2 or end1)
    


    color1 = histos1.copy()
    color2 = histos2.copy()

    
    

        

    #can compare user and copy 
    x+=1


#use this method up in the check stability 



cu1 = Counter(color1).most_common()
cu2 = Counter(color2).most_common()
cu1.sort()
cu2.sort()



result = True

conclusion1 = []
conclusion2 = []
#extract

if len(cu1) == len(cu2):
    c1 = lambda l: list(map(lambda c: c[1], l)).sort()
    conclusion1 = c1(cu1)
    conclusion2 = c1(cu2)
    if conclusion1 == conclusion2:
        print("We cannot conclude that they are different")
    else:
        print("We can conclude that they are different")
else:
    print("We can conclude that they are different")
#compare and conclusion


