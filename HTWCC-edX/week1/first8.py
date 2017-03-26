# first week - problem 7
#import time

#start_time = time.time()

f = open('input.txt', 'r')
l=int(f.readline())
t_list=f.readline()
t=list(int(x) for x in t_list.split())


t.sort()
max_time=18000
exam_time=0
maxProb=0
for x in t:
    #print("exam_time", exam_time)
    exam_time+=x
    
    if exam_time > max_time:
        break
    maxProb+=1
    

#print("maxProb: ", maxProb)

fout=open('output.txt', 'w')
fout.write(str(maxProb))
f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
