#This is a comment and ignored by python
first_string = "This is a string"
first_number = 5

second_string = first_string + " and this is another string" #notice the space in the added string
second_number = first_number + 5 #should be 10
first_and_second_multiplied = first_number * second_number

print(first_string)
print(second_string)
print(first_number)
print(second_number)
print(first_and_second_multiplied)
print(first_and_second_multiplied)
print(first_and_second_multiplied)
print(first_and_second_multiplied)

#Need to convert numbers to print them with strings
print(second_string + " " + str(second_number))

for x in range(0,20):
    print("Hello World")