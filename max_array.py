n=int(input())
ar=list(map(int,input().split()))
sum1=0
sum2=0
for i in ar:
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
print(sum1,sum2)0
        
