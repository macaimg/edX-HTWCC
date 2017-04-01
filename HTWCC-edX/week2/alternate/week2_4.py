# first week - problem 7
#import time

#start_time = time.time()

f = open('input.txt', 'r')
fout=open('output.txt', 'w')

l=int(f.readline())

def checkSeq(line):
    
    #print(line[0])
    
    if line[0] == ')' or line[0] == ']' or len(line) % 2 != 0:
        return "NO"
    
    priv = ""
    
    while (len(line) != len(priv)):
        priv = line
        line = line.replace("()", "")
        line = line.replace("[]", "")
        
    if len(line) == 0:
        return "YES"
    else:
        return "NO"

for x in range(0, l):
    line = f.readline()
    
    flag = checkSeq(line.rstrip())
    #print(flag)
    fout.write(flag + '\n')

f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
