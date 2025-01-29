import random
def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  color =(["red", "green", "yellow", "blue"])
  sides = (["left", "right"])
  appendage = (["hand", "foot"])

# Here's the function call. This should print a random assortment of twister commands
  for i in range(10):
    print(random.choice(color))
    print(random.choice(sides))
    print(random.choice(appendage))
    print("\n")
print(spin_twister_spinner())