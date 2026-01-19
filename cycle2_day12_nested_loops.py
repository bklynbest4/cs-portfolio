# Gemini Guided Question

for row in range(1, 6):
    # Now were inside the loop (The mason's job)
    for brick in range(1, row + 1):
        print(brick, end=" ")
    print()


# Independant Practice

stars= "*"

for row in range(5, 0, -1):
    for star in range(row):
        print(stars, end= " " )
    print()
    
# Gemini Guided Help


for row in range(1, 4):          # Manager: Pick Row 1, 2, or 3
    for col in range(1, 4):      # Mason: Pick Column 1, 2, or 3
        product = row * col      # Calculate the "Cell Value"
        print(product, end="\t") # Print value + a "Tab" space to keep columns straight
    print()                      # Manager: Move to the next row



def multiply_numbers(a, b):
    product= a * b
    return product 
my_result = multiply_numbers(3, 4)
