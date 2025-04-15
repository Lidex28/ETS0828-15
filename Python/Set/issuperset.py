# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3}

# Check if set_a is a superset of set_b
is_superset = set_a.issuperset(set_b)

print("Is set_a a superset of set_b?", is_superset)


# Define two sets
set_x = {1, 2, 3, 4}
set_y = {1, 2, 3, 4}

# Check if set_x is a proper superset of set_y
is_proper_superset = set_x.issuperset(set_y) and set_x != set_y

print("Is set_x a proper superset of set_y?", is_proper_superset)
