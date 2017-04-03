# 2nd week - problem 6
#import time
#import copy

#start_time = time.time()

f = open('input.txt', 'r')
fout=open('output.txt', 'w')

l=int(f.readline())

totalSumStack = []
topEleStack = {}
inputStack = []

totalMass = 0

# for the first operation
acts = (f.readline()).split()
totalSumStack.append(int(acts[1]))
topEleStack[0] = [int(acts[1])]


#print("totalSumStack: ", totalSumStack)
    
# for rest of the operations
for x in range(1, l):
    acts = (f.readline()).split()
    
    act = int(acts[0])
    desc = int(acts[1])
    inputStack.append([x, act])
    
    if act == 0:
                
        topEleStack[x] = [desc]
        totalSumStack.append(desc)
            
    elif desc == 0:
        stack = list(topEleStack[act - 1])
        topElementToPop = stack.pop()
        topEleStack[x] = stack
        
        totalSumStack.append(totalSumStack[act-1] - topElementToPop)
        
    else:
        #stack = copy.copy(topEleStack[act - 1])
        stack = list(topEleStack[act - 1])
        stack.append(desc)
        topEleStack[x] = stack
        
        totalSumStack.append(totalSumStack[act-1] + desc)
    
#print("totalSumStack: ", totalSumStack)
#print("topEleStack: ", topEleStack)   

for x in range(0, len(totalSumStack)):
    totalMass = totalMass + totalSumStack[x]
#print(totalMass)

fout.write(str(totalMass))
f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
