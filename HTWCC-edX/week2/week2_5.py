# 2nd week - problem 5
#import time

#start_time = time.time()

f = open('input.txt', 'r')
fout=open('output.txt', 'w')

l=int(f.readline())

stack = []

exp = (f.readline()).split()

for x in range(0, l):
    noo = exp[x]
    if noo == '+':
        res = stack.pop() + stack.pop()
        stack.append(res)
    elif noo == '-':
        right = stack.pop()
        left = stack.pop()
        res = left - right
        stack.append(res)
    elif noo == '*':
        res = stack.pop() * stack.pop()
        stack.append(res)
    else:
        stack.append(int(noo))  
    
    #print(stack)
    
#print(stack.pop())

fout.write(str(stack.pop()))
f.close()
fout.close()

#print("--- %s seconds ---" % (time.time() - start_time))
