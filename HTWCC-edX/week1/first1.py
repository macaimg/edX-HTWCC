f = open('input.txt', 'r')
inputStr=f.readline()
v=inputStr.split()
outVal=int(v[0])+int(v[1])
fout=open('output.txt', 'w')
fout.write(str(outVal))
f.close()
fout.close()


