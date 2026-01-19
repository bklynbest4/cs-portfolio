for i in range(30):
    if i % 3 == 0: # CHeck if divisble by 3 
        print(i)


count = 100

while count >= 0:
    if count % 2 == 0: 
        print(count)
    count -= 2


temps = [68, 72, 80, 65, 90, 71, 85]

for temp in temps: # Loop through each temperature
    if temp > 75:  # Check if this temperature is hot
         print(f"Warning: {temp} F is hot!!")


for i  in range (1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")