# first week - problem 7
#import time

#start_time = time.time()

f = open('input.txt', 'r+')
fout=open('output.txt', 'w')

l=int(f.readline())

stackList=[]
ansList = []
popList = ''
for x in range(0, l):
    line = f.readline()
    op = line.split()
    
    if len(op) == 2:
        stackList.append(op[1])
    else:
        stackSize = len(stackList)
        ansList.append(int(stackList[stackSize - 1]))
        stackList.pop()
        
for x in ansList:
    fout.write(str(x) + '\n')

f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
