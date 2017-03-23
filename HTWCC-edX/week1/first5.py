# first week - problem 5

f = open('input.txt', 'r')
a=f.readline()

n=list(int(x) for x in a.split())


total_distance=0



for p in range(0,3):
    total_distance+=n[p]
    
    
#print(total_distance)
    
final_ans=total_distance/6
#print(final_ans)
fout=open('output.txt', 'w')
fout.write(str(final_ans))
f.close()
fout.close()
