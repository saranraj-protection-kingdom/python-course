num1=int(input("Enter the range 1"))
num2=int(input("Enter the range 2"))
for num in range(num1,num2 + 1):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if num == sum:
       print(num)
