# #1
students = ["claude", "sucre", "paul"]
# print(students[1])
# print(students[2])
# #2
fruits = ('mango','strawberry', 'mangosteen' )
# #3
# for fruit in fruits:
#     print(fruit)
#4
home_town = {

    "city": "chicago",
    "state": "illinois",
    "population": "actually dont know the population"
   

}

# print(f'i was born in {home_town["city"]} in the state of {home_town["state"]} and {home_town["population"]}')


#5
for key, value in home_town.items():
    print(key,value)


#6 
stardust = []
for student, fruit in zip(students, fruits):
    student_collection = {"name": student, "fruits": fruit}

stardust.append(student_collection)

print(stardust)
