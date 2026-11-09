r=0
while (r<10):
 r+=1
 print('* - pr21.py:4'+str(r))
 if r==4 : continue
 if not r % 2 : r+=2
 if r==5 : break
 print(r)
print(r)
print("\nСколько раз сработал цикл? > - pr21.py:10")
print(r)