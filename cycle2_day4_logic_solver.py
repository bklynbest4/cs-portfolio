# Truth Table Validator
# Cycle 2, Day 4 - Jonathan Liu
# Tests basic Boolean logic operations

print("=== LOGIC PUZZLE SOLVER ===\n")

# Puzzle 1: AND operator
print("Puzzle 1: You can drive if you have a license AND you're 18+")
has_license = True
is_18_or_older = False

# YOUR CODE HERE: Check if person can drive (both must be True)
# Store result in variable: can_drive
# Print "Can drive" or "Cannot drive"

if has_license and is_18_or_older:
    print("Can drive")
else:
    print("Cannot drive")


# Puzzle 2: OR operator  
print("\nPuzzle 2: Store is open on Saturday OR Sunday")
today = "Monday"

# YOUR CODE HERE: Check if store is open
# Store result in variable: is_open
# Print "Open" or "Closed"

if today == "Saturday" or today =="Sunday":
    print("Open")
else:
    print("We're closed")

# Puzzle 3: NOT operator
print("\nPuzzle 3: Access denied if user is NOT verified")
is_verified = False

# YOUR CODE HERE: Check if access should be denied
# Print "Access Denied" or "Access Granted"
if not is_verified:
    print("Access denied")
else:
    print("Access granted")

# Puzzle 4: Combined logic (AND + OR)
print("\nPuzzle 4: Can board plane if (has ticket AND has ID) OR is_crew")
has_ticket = True
has_id = False
is_crew = False

# YOUR CODE HERE: Check if person can board
# Print "Can board" or "Cannot board"

if has_ticket and has_id or is_crew:
    print("Can board")
else: 
    print("Cannot board")

print("\n=== All puzzles complete! ===")