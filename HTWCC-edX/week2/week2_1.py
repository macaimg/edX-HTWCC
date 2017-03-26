# first week - problem 7
#import time

#start_time = time.time()

f = open('input.txt', 'r')
fout=open('output.txt', 'w')

l=int(f.readline())

stackList=[]
ansList = []
popList = ''
for x in range(0, l):
    line = f.readline()
    op = line.split()
    #print(len(op))
    
    if len(op) == 2:
        stackList.append(op[1])
    else:
        stackSize = len(stackList)
        #print("stack length" )
        #print(stackList[stackSize-1])
        #popList+=stackList[stackSize-1]+'\n'
        #fout.writelines(stackList[stackSize-1]+'\n')
        ansList.append(str(stackList[stackSize - 1]))
        stackList.pop()
        
#popList.rstrip('\n')
#print(popList)
#popList = popList[:-1]
#fout.write(popList)
#print(stackList)
#lines = fout.readlines()

#lines = lines[:-1]

for x in ansList:
    print(x, file=fout)



f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
