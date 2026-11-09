r=0
while (r<10):
 r+=1
 print('*'+str(r))
 if r==4 : continue
 if not r % 2 : r+=2
 if r==5 : break
 print(r)
print(r)