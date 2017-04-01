# first week - problem 7
#import time

#start_time = time.time()

f = open('input.txt', 'r')
fout=open('output.txt', 'w')

l=int(f.readline())


def isMatchingPair(bracket):
    topElement = stack.pop()
    #print("popped item : ", topElement, "  bracket : ", bracket)
    if topElement == '(' and bracket == ')':
        return True
    elif topElement == '[' and bracket == ']':
        return True
    else:
        return False
    

def checkSeq(line):
    
    #print(line[0])
    
    if len(line) % 2 != 0:
        return "NO"
    
    seqlen = len(line)
    for x in range (0, seqlen):
        #print(stack)
        bracket = line[x]
        
        if bracket == '(' or bracket == '[':
            stack.append(bracket)
        elif bracket == ')' or bracket == ']':
            if len(stack) == 0:
                return "NO"
            else:
                ifMatching = isMatchingPair(bracket)
                if ifMatching == False:
                    return "NO"
                
        
    if len(stack) == 0:
        return "YES"
    else:
        print(stack)
        return "NO"

bracketCheckList = []

for x in range(0, l):
    stack = []
    line = f.readline()
    
    flag = checkSeq(line.rstrip())
    #print(flag)
    bracketCheckList.append(flag);

for flag in bracketCheckList:
    fout.write(flag + '\n')

f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
