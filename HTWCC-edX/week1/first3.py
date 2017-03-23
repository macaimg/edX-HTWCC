# first week - problem 3
f = open('input.txt', 'r')
no_of_days=int(f.readline())
pi=f.readline()
ti=f.readline()

pil=list(int(x) for x in pi.split())
til=list(int(x) for x in ti.split())

total=0
pil_sum=0
til_sum=0
min_diff=1000
min_diff_index=0
p_flag=0
t_flag=0

for x in range(0,no_of_days):
    p=pil[x]
    t=til[x]
    diff=0
    if p > t:
        total = total + p
        diff = p - t
    elif t > p:
        total = total + t
        diff = t - p
    else:
        total = total + t
        
    pil_sum+=p
    til_sum+=t
    if diff < min_diff:
        min_diff = diff
        min_diff_index = x
    

#print("total sum : ",total)
#print("pil sum : ", pil_sum)
#print("til sum : ", til_sum)
#print("min_diff: ", min_diff)
#print("min_diff_index: ", min_diff_index)

final_ans=total

if (pil_sum == total) | (til_sum == total):
    final_ans = total - min_diff
    #print("correct ans: ", str(final_ans))

#outVal=int(v[0])+(int(v[1]) * int(v[1]))
fout=open('output.txt', 'w')
fout.write(str(final_ans))
f.close()
fout.close()
