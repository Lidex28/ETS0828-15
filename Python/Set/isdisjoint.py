set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

# Check if set1 and set2 are disjoint (no common elements)
print(set1.isdisjoint(set2))  # Output: True (no overlap)

# Check if set1 and set3 are disjoint
print(set1.isdisjoint(set3))  # Output: False (both have '3')