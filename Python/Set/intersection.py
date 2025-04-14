# Create two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# Apply intersection_update()
setA.intersection_update(setB)

print("Updated setA:", setA)  # Original setA is modified
print("setB remains unchanged:", setB)