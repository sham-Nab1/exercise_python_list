# student_name_list.py

# list of 20 student names.
student_names= [
    "Sham", "Jane", "Mel", "Cess", "Althea", "Rose", "Leigh", "Ella", "Ivy", "Rachel",
    "Angelyn", "Jia", "Angel", "Earl", "Dens", "Chris", "Ram", "Kisser", "Kyle", "John"
]

# Print the entire list.
print("Student Names :")
print(student_names)

# Access and print the 15th index.
print()
print("15th index is :", student_names[14])

# Update the 12th index to "Imee".
student_names[11] = "Imee"
print()
print ("Updated list after changing 12th index to 'Imee': ")
print(student_names)

# Delete the 10th index.
del student_names[9]
print()
print ("Updated list after deleting the 10th index: ")
print(student_names)

# Slice the list from index 2 to 5 and print the sliced portion.
sliced_list = student_names[2:6]
print()
print("Sliced portion from 2 to 5: ")
print(sliced_list)

# Print the last index of the list.
print()
print("Last index is: ", student_names[-1])