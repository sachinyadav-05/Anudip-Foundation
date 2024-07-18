# Diplay list Without any formatting-
l=[20,20,60,'lucky',52]
print("list is -" ,*l)


# Accesing members using for loop-
l=[20,20,60,'lucky',52]
for i in l:
    print(i)

#Fetching  element
l=[10,20,60,'lucky',52]
print("third element is",l[2])#using forward indexing
print("last element using backword indexing",l[-5])#using backword indexing
print("from 2 to 5",l[2:5])#slicing / more than one element
print("fetching alternate element",l[0:5:2])

#Q-1- print elements in backward direction using forward index
l=[20,50,12,12,85,48,12,63,17,12,82,15,20,75,25,12,48,63,60,90]
n=len(l)-1
print("Elements are --")
# method one -print(l[20::-1])
#mwthod 2-
for i in range(n,-1,-1):
    print(l[i] , end = " , ")

#INSERTING  elements in list
#1- Insertion at end -
l=[20,50,12,12,85,48,12,63,17,12,82,15,20,75,25,12,48,63,60,90]
l2=[1,2,3]
l3=[12,52,62]
print(l)
x=int(input("Enter any number :-  "))#append method 
l.append(x)#append method
print("updated list is :- " ,l)
l.append(l2)
print("merged list:- ",l)
#Extend() method
l.extend(l3)
print(l)

# 2- Insert at specified postion-
l=[20,50,12,12,85,48,12,63,17,12,82,15,20,75,25,12,48,63,60,90]
l.insert(5,3)
print(l)



#Removing element from list
#1- pop()- 
l=[20,50,12,12,85,48,12,63,17,12,82,15,20,75,25,12,48,63,60,90]
l.pop()
l.pop(2)
print(l)
#2- remove() -
l.remove(20)
print(l)


    

