a=4
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
if sum==a:
        print(f" { a} is a perfect number")
else:
    print(f" { a} is not a perfect number")
    
