# first week - problem 7
import time
import math
from functools import reduce
start_time = time.time()

f = open('input.txt', 'r')
input_field=int(f.readline())

max_div_num=0
x_pointer=0
maximal=0

def get_divisors(n):
    divisors=0
    for x in range(1,round((n+1)/2)):
        if n%x == 0:
            divisors+=1
    return divisors+1

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
    # n = 9999999
    #maximal week1 279280
    #--- 47.02463364601135 seconds ---

def divisors(n):
    divs=[1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    return len(list(set(divs)))

def factorGenerator(n):
    if n <= 1: return []
    prime = next((x for x in range(2, math.ceil (math.sqrt(n))+1) if n%x == 0), n)
    return [prime] + factorGenerator(n//prime)

def factorgen(n):
    if n <= 1: return
    prime = next((x for x in range(2, math.ceil(math.sqrt(n))+1) if n%x == 0), n)
    yield prime
    yield from factorgen(n//prime)

def divisorGen(n): # best one in stackoverflow
    factors = factorgen(n)
    #print(factors)
    nfactors = len(list(factors))
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


#gen=factorgen(12)
gen=divisorGen(12)
print("gen", gen) 



start_range=round(input_field/2)
end_range=input_field+1
#start_range=0

for x in range(start_range,input_field+1):
    
    #m_div=get_divisors(x)
    m_div=len(list(divisorGenerator(x)))
    #m_div=divisors(x)
    #print("Before if: ... x = ", x, " m_div = ", m_div, "max_div_num= ", max_div_num)
    if m_div > max_div_num:  
        #print("inside if..")      
        max_div_num = m_div
        x_pointer = x
    #print(" x = ", x, ", m_div = ", m_div, ", max_div_num = ", max_div_num)
    #print(" ")  
    
maximal  = 1 + input_field - x_pointer

#print("max_div_num: ", max_div_num)
#print("x_pointer: ", x_pointer) 
print("maximal week1", maximal)

fout=open('output.txt', 'w')
fout.write(str(maximal))
f.close()
fout.close()

print("--- %s seconds ---" % (time.time() - start_time))
