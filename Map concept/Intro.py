user_input = input("Enter numbers separated by space: ")

# Convert the string of numbers into a list of integers
numbers = map(int, user_input.split())
updated=map(lambda x:x+2,numbers)
print(list(updated))
             


# s="lokal"
# print(s[-1])