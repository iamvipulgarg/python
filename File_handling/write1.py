p=open('a3.txt','a')
p.write('\nHii');
l1=['\n','10 ','20 ',' 30']
p.writelines(l1)
l2=[1,2,3,4,5,6,7,8,9]
for i in l2:
    p.write('\n')
    p.write(str(i))