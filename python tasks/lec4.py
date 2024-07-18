#tuple
numbers = (1,2,3,4,5)
#print(numbers[4::-1])
n=len(numbers)-1
for i in range(n,-1,-1):
    print(numbers[i] , end = " , ")

#Dictionary
student={ 'std':'std01','stdname':'lucky','education':'B-Tech'}
print(student)
print(*student)

print("------------------------")
#insert element
student['education']='M-Tech'
print(student)
student['sub']='Computer'
print(student)

print("------------------------")
#access key
for i in student:
    print(i)

print("---------------------------------------")
#to find value 
for key in student:
    print(student[key])

print("------------------------")
#print in format
for key in student:
    print(key," - ",student[key])

print("------------------------")
#access value
print("education is :  ",student['education'])

print("------------------------")
# Sort by key
sorted_d = dict(sorted(student.items()))
print(sorted_d)

#keys()= it will return a list of keys of all the element of dictionary.
student={ 'std':'std01','stdname':'Lucky','education':'B-Tech'}
student2={'std':'std02','stdname':'Shivam','education':'Bca','Age':24}
elementskey =student.keys()
print(elementskey)

#- values()= it will return a list of all the values of all the elements of dictionary
print("--------------------------")
elementsvalue= student.values()
print(elementsvalue)

#items() =  it will returns a list of items(each item will be in the form of tuple with two mwmbers (i.e. key - value)
print("---------------------------------------")
elements=student.items()
print(elements)

#get() - return specfied key
print("-----------------------")
x= student.get('hindi','no elemnt exist')#if no elemt give 2nd arg you pass
print(x)

#update() - update  or insert multiple elements (in  the key-value pair) in the dict.(2nd dict in 1)
print("------------------------")
student.update(student2)
print(student)

#fromkeys() - return a dict with specfied keys and values
print("-------------------")
x=student.fromkeys('education','name')
print(x)
y=student.fromkeys(student.keys(),student2.values())
print(y)