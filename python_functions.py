#deliverable homework
#1
# n = int(input('input number'))

# def sum_to(n):
   
#     print (n*(n+1)//2)

# sum_to(n)

#2
# n = [0,2,4,5,6]

# def largest(n):
#     # sorting the list
#     n.sort()

#     # printing the last element
# print("Largest element is:", n[-1])


# #3
# def occurances(phrase1, phrase2):
#     return (phrase1).count(phrase2)


# print(occurances('fleep', 'floop'))

#4
def product(*args):
    total = 1
    for num in args:
        total *= num
    return total
print(product(-1,4))




