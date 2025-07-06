# Tupple ae readonly form of list, () optional, duplicasy allowed,comma seprated

"""
    1) wap to find duplicate elemensts form tuple
    2) 
    3) 

"""
t1 = (10,20,30) #Tuple
t2 = 10,20,30 #Tuple
t3 = (10) #Int
t4 = (10,) #Tuple

t5 = (10,20,40,44,50,30,10,20,10,20,30,40)

checked=[]
dup = []
for i in t5:
    if i in checked:
        if i not in dup:
            dup.append(i);
    else:
        checked.append(i);
        
            
            

print(dup)
