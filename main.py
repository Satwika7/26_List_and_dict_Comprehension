#list comprehension
#it is basically getting the list from existing list
#for example we have a list and we need a newlist with eachelement+1 of old list in new list then we dont have to iterate we have a list comprehension technique

numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

#we can even get it from a string
name = "sam"
letters_list = [letters for letters in name]
print(letters_list)

double_nums = [2*number for number in range(1,5)]
print(double_nums)


#conditional list comprehension

nums = [1,5,8,20,67,90,5,4]
req_nums = [ele for ele in nums if ele<=10]
print(req_nums)


#Dictionary comprehension

import random
names = ["a","b","c","d","e","f","g"]
student_scores = {item:random.randint(10,50) for item in names}
print(student_scores)


#conditional Dictionary comprehension
#here student_scores is a dictionary

passed_students = {name:scores for (name,scores) in student_scores.items() if scores>30 }
print(passed_students)


#iteration over dataframes in pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)

#we have a method iterrows in pandas to go through rows in dataframe

import  pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print(index)
    print(row)
    #Access row.student or row.score
    print(row.student)
    print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}





