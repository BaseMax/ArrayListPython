from ArrayList import ArrayList

# Create a new list
list = ArrayList(10)

# Add items to the list
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)

# Print the list
print(list)

# Remove an item from the list
list.remove(3)

# Print the list
print(list)

# Check if an item is in the list
print(list.search(3))
print(list.search(4))

# Get an item from the list
print(list.get(2))

# Print the length of the list
print(len(list))

# Print the list
print(list)

# Iterate over the list
for item in list:
    print("\t", item)
