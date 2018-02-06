num1 = int(input())
lst=[]
count=0
for i in range(0,num1):
    tot=int(input())
    count+=tot
    lst.append(tot)
print(int(count/num1))
