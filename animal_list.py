# animal_list.py

# List of 10 animal names.
animal_names= [
    "Butterfly", "Dog", "Bird", "Duck", "Cat", 
    "Fish", "Kangaroo", "Mouse", "Lion", "Snake", 
]

# Print all list of animal names.
print("Animal List: ")
print(animal_names)

#Access and print the 3rd index.
print()
print("3rd index is:" , animal_names[2])

# Update the 6th index to "Elephant".
animal_names[5]= "Elephant"
print()
print("Updated list after changing the 6th index to 'Fox': ")
print(animal_names)

# Delete the 8th index.
del animal_names[7]
print()
print("Updated list after deleting the 8th index: ")
print(animal_names)

# Print the last index.
print()
print("last index is: ", animal_names[-1])