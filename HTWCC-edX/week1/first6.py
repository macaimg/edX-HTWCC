# first week - problem 6

def find_coordinates(c):
    coordinates=[]      
    for k, v in keyboard.items():
        if c in v:
            coordinates.append(k)
            coordinates.append(v.index(c))
    #print(coordinates)
    return coordinates  

def get_time_to_type(template):
    totaltime=0
    
    for t in range(0, (len(template)-1)):
        a=find_coordinates(template[t])
        b=find_coordinates(template[t+1])
        
        #print("a, b: ", a, b)
        
        dist_between_keys=max((abs(a[0]-b[0])), abs(a[1]-b[1]))
        
        totaltime+=dist_between_keys
    
    return totaltime
        

f = open('input.txt', 'r')
kbConf=f.readline()

confList=list(int(x) for x in kbConf.split())

x=confList[0]
y=confList[1]

#print(x,y)

keyboard = {}

for x in range(0,y):    
    xlist=f.readline().strip()
    keyboard[x]=list(xlist)
    #print(keyboard[x])


langs={}
templates={}
best_time=99999999999
lang_key=0

emptyFlag=0
for t in range(0,3):
    time_to_type=0
    lang=f.readline()
    langs[t]=lang.strip()
    #print("language: ", lang)
    tline=f.readline()
    template=""
    while (tline.strip() != '%TEMPLATE-END%'):
        if tline.strip() == '%TEMPLATE-START%':
            tline=f.readline()
            continue
        template+=tline.replace(" ","").replace("\n","")
        tline=f.readline()
    #print(template)
    templates[t]=template
    time_to_type=get_time_to_type(template)
    
    if time_to_type < best_time:
        best_time = time_to_type
        lang_key = t
    
#print("templates: ", templates)
#print("best time: ", best_time)
#print("best lang: ", langs[lang_key])


fout=open('output.txt', 'w')
fout.write(str(langs[lang_key])+"\n")
fout.write(str(best_time))
f.close()
fout.close()
