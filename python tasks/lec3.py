# UNDERSTANDING TUPLE AND SOLVING A PROBLEM GIVEN BELOW ON DATA FROM EXCEL.-
data = [
    ["stdid", "stdname", "standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"],
    ["std101", "Ashish Kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
    ["std102", "Abhishek Kumar", "10th", 14, 90, 90, 90, 45, 45, 360],
    ["std103", "Aman", "10th", 15, 67, 56, 78, 78, 45, 313],
    ["std104", "Rahul", "10th", 15, 89, 56, 45, 45, 67, 302],
    ["std105", "Ruby", "10th", 13, 78, 90, 67, 45, 56, 336],
    ["std106", "Suman", "10th", 15, 90, 45, 67, 67, 67, 403],
    ["std107", "Saurabh", "10th", 15, 45, 23, 34, 78, 90, 270],
    ["std108", "Sumit", "10th", 15, 78, 90, 67, 78, 78, 391],
    ["std109", "Kamlesh", "10th", 15, 45, 78, 56, 67, 67, 303],
    ["std110", "Rohan", "10th", 15, 12, 24, 45,56,34,171]
]
#1-Student having marks more than 50 in english:-
print("Student having marks more than 50 in english:-")
for row in data[1:]:
    if row[5]>50:
        print(row[1])

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")


#2-Student name and age of top four scrorer in maths:-


print("Student name and age of top four scrorer in maths:-")
data_rows = data[1:]
# Sort the data rows by the 'Maths' column (index 6) in descending order
sorted_data = sorted(data_rows, key=lambda x: int(x[6]), reverse=True)
# Get the top 4 scorers
top_4_scorers =sorted_data[:4]
print("Top 4 scorers in Math are:")
for row in top_4_scorers:
  print(f"Name: {row[1]}, Age: {row[3]}")

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")


# 3- bottom 3 scorers in computer are:-


data_rows2 = data[1:]
sorted_data2 = sorted(data_rows, key=lambda x: int(x[8]), reverse=False)

bottom_3 = sorted_data2[:3]
print("bottom 3 scorers in computer are:")
for row in bottom_3:
    print(row[0],row[1],row[3])




