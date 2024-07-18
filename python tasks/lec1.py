#QUESTION 1
#Calculate sum and average of number present in a list.
l=[80,90,30,20,70,80,39,87]
s=0
for x in l:
    s = s+x
print("sum is - " , s)
print("Average is - ",s//len(l)

# question 2
# display number btw 10 to 500 divisible by 10 and 7

'''for i in range(10,500):
    if(i % 7 ==0 and i % 10 == 0):
        print(i)'''


#question3
# count the number between 100 to 1000 which is even and divisible by 3
print("Number between 100 to 1000 which are even and divisible by 3")
count = 0
for i in range(100,1000):
    if(i%2==0 and i%3 ==0):
        print(i,end =" , " )
        count += 1
print("total numbers are - ",count,end =" ," )