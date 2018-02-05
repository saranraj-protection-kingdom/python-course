num1 = raw_input()
lst=(num1.split(' '))
count=0
for i in range (0,len(lst)):
    ele=lst[i]
    length=len(ele)
    count+=length
print count
