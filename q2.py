# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
#Eagle, Elephant, Eel, Elk, Earthworm
animal = random.choice (["Eagle", "Elephant", "Eel", "Elk", "Earthworm"])
# Age (integer)
age = random.randint (1, 214)
# Color (at least 3 choices, string)
color = random.choice (["Red", "Royal Blue", "Golden", "Amber", "Teal", "Ice Blue", "Vomit green"])
# Weight (float)
weight = random.uniform (1, 3002)

# Print a summary of your pet using an f-string
print(f"Your pet is a {color} {animal}, weighing at {weight} pounds at only {age} years old")