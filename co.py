# count
sum=0
for num in range(2,10):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
        	sum=sum+1
print(sum)
