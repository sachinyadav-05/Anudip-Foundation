# PROBLEM ON DICTIONARY:-
Students = {
           'data1': {
            'stdid': 'std101', 'stdname': 'Ashish Kumar', 'standard': '10th', 'Age': 15,
            'Hindi': 67, 'English': 89, 'Maths': 87, 'Science': 89, 'Computer': 90, 'Total': 422
            },
            'data2':{
                'stdid': 'std102', 'stdname': 'Abhishek Kumar', 'standard': '10th', 'Age': 14,
                'Hindi': 90, 'English': 90, 'Maths': 90, 'Science': 45, 'Computer': 45, 'Total': 360
            },
             'data3':{
                'stdid': 'std103', 'stdname': 'Aman', 'standard': '10th', 'Age': 15,
                'Hindi': 67, 'English': 56, 'Maths': 78, 'Science': 78, 'Computer': 45, 'Total': 313
            },
             'data4':{
                'stdid': 'std104', 'stdname': 'Rahul', 'standard': '10th', 'Age': 15,
                'Hindi': 89, 'English': 56, 'Maths': 45, 'Science': 45, 'Computer': 67, 'Total': 302
            },
             'data5':{
                'stdid': 'std105', 'stdname': 'Ruby', 'standard': '10th', 'Age': 13,
                'Hindi': 78, 'English': 90, 'Maths': 67, 'Science': 45, 'Computer': 56, 'Total': 336
            },
            'data6':{
                'stdid': 'std106', 'stdname': 'Suman', 'standard': '10th', 'Age': 15,
                'Hindi': 90, 'English': 45, 'Maths': 67, 'Science': 67, 'Computer': 67, 'Total': 403
            },
             'data7':{
                'stdid': 'std107', 'stdname': 'saurabh', 'standard': '10th', 'Age': 15,
                'Hindi': 45, 'English': 23, 'Maths': 34, 'Science': 45, 'Computer': 34, 'Total': 181
            },
             'data8':{
                'stdid': 'std108', 'stdname': 'Sumit', 'standard': '10th', 'Age': 15,
                'Hindi': 78, 'English': 90, 'Maths': 67, 'Science': 78, 'Computer': 78, 'Total': 391
            },
            'data9':{
                'stdid': 'std109', 'stdname': 'Kamlesh', 'standard': '10th', 'Age': 15,
                'Hindi': 45, 'English': 78, 'Maths': 56, 'Science': 67, 'Computer': 67, 'Total': 303
            },
            'data10':{
                'stdid': 'std110', 'stdname': 'Rohan', 'standard': '10th', 'Age': 15,
                'Hindi': 12, 'English': 24, 'Maths': 45, 'Science': 56, 'Computer': 34,'Total':171
            }
 }
for key, value in Students.items():
    if value['English'] > 50:
        print(value['stdname'])

# Extract Maths scores and corresponding student details
math_scores = [(value['Maths'], value['stdname'], value['Age']) for value in Students.values()]

# Sort based on Maths scores in descending order
math_scores.sort(reverse=True, key=lambda x: x[0])

# Get top four scorers
top_four_scorers = math_scores[:4]

# Display the names and ages of top four scorers
for score, name, age in top_four_scorers:
    print(f"Name: {name}, Age: {age}")