# first week - problem 4

import math

f = open('input.txt', 'r')
a=f.readline()
b=f.readline()
c=f.readline()
n=list(int(x) for x in a.split())
p=list(int(x) for x in b.split())
u=list(int(x) for x in c.split())

bp=[n, p, u]
bestCase=0
total=0

def sq(i):
    return i*i

for p in range(3,0):
    print(p)

for x in range(0,3):    
    for y in range(0,3):
        total=sq(int(bp[x][y]))
        total2=total
        #print("x,y: ", x, ",",y)
        flag1=0
        flag2=0
        used_q=100
        used_p=100
        for m in range(0,3):
            
            if (x != m):
                #print("z - ", z)
                m_flag=0
                for p in range(0,3):
                    p=2-p
                    if used_p == p:
                        continue
                    if (y != p) & (m_flag == 0):
                        total2=total2 + sq(int(bp[m][p]))
                        #print("y,q: ", y,",",q)
                    
                        #print("m,p: ", m,",",p)
                        m_flag=1
                        used_p=p
        for m in range(0,3):
            
            if (x != m):
                #print("z - ", z)
                m_flag=0         
                for q in range(0,3):
                    if used_q == q:
                        continue
                    if (y != q) & (m_flag == 0):
                        total=total + sq(int(bp[m][q]))
                        #print("y,q: ", y,",",q)
                    
                        #print("m,q: ", m,",",q)
                        m_flag=1
                        used_q=q       
                    
                        
        #print("total: ", total)
        #print("total2: ", total2)
        #print("     ")
        
        if bestCase < total:
            bestCase = total
        elif bestCase <total2:
            bestCase = total2
        
#print("bestcase: ", bestCase)
    


final_ans=math.sqrt(bestCase)
#print(final_ans)
fout=open('output.txt', 'w')
fout.write(str(final_ans))
f.close()
fout.close()
