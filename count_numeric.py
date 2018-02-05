num1 = raw_input()
lst=map(None,num1)
print lst
count=0
for i in range (0,len(lst)):
    ele=lst[i]
    if ele.isnumeric():
        count+=1
print count
