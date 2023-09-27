def calculate_square_footage(length, width):
  return length * width
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
square_footage = calculate_square_footage(length, width)
print(f"The square footage of the house is {square_footage} square feet.")
