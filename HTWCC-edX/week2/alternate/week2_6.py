# 2nd week - problem 5
#import time

#start_time = time.time()

f = open('input.txt', 'r')
fout=open('output.txt', 'w')

l=int(f.readline())

totalSumStack = []
topEleStack = {}
inputStack = []
#totalSumStack.append(0)
totalMass = 0

# for the first operation
acts = (f.readline()).split()
totalSumStack.append(int(acts[1]))
topEleStack[0] = [int(acts[1])]
inputStack.append([0, int(acts[0])])

# for rest of the operations
for x in range(1, l):
    acts = (f.readline()).split()
    
    act = int(acts[0])
    desc = int(acts[1])
    inputStack.append([x, act])
    print(acts)
    #print("before ... topEleStack: ", topEleStack)
    
    stack = topEleStack[x-1]
    if desc == 0:
        #print("totalsumStack: ", totalSumStack[act-1])
        topElementToPop = stack.pop()
        print("totalSumStack[act-1]: ", totalSumStack[act-1])
        print("topElementToPop: ", topElementToPop)
        totalSumStack.append(totalSumStack[act-1] - topElementToPop)
        topEleStack[x] = topEleStack[act-1]
        
    else:
        totalSumStack.append(totalSumStack[act-1] + desc)
        stack.append(desc)
        topEleStack[x] = stack
        #inputStack.append([act, desc])
    #print("after ... topEleStack: ", topEleStack)
    #print("topEle: ", topEleStack[act-1])
    #print("totalSumStack: ", totalSumStack)
    print(stack)
    print("\n")    
    #print("topEleStack: ", topEleStack)       
    #print("inputStack: ", inputStack)
    
#print(inputStack)   
    
#print("totalSumStack: ", totalSumStack)
print("topEleStack: ", topEleStack)   

for x in range(0, len(totalSumStack)):
    totalMass = totalMass + totalSumStack[x]
print(totalMass)

fout.write(str(totalMass))
f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
