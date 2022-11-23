#WAP to build a tuple T1 containing ages ranging from 10 to 70 with a gap of 5 years in between. 
# Extract a tuple T2 containing ages below 30. Extract another tuple T3 containing ages above 30 
# but below 50 and extract another tuple T4 having ages above 50. Use Tuple comprehension.

t1=tuple([x for x in range(10,71,5)])
t2= []
t3=[]
t3=[]
t4=[]
ext3=[]
print(t1)
for i in t1:
    if i < 30:
        t2.append(i)
print("Ages below 30 : ",t2)
for i in t1:
    if i > 30:
        ext3.append(i)
        
for j in ext3:
    if j < 50:
        t3.append(j)
print("Ages above 30 : ",t3)

for k in t1:
    if k > 50:
        t4.append(k)
print("Ages above 30 : ",t4)