num1 = raw_input()
lst=map(None,num1)
length=len(lst)
print lst
count=0
for i in range (0,len(lst)):
    ele=lst[i]
    if ele.isalpha():
        count+=1
print length-count
