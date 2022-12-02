# ArrayList Python

This is a simple implementation of ArrayList in Python.

## Functions

-   `add` - Add an element to the end of the list
-   `add_at` - Add an element at a specific index
-   `remove` - Remove an element from the list
-   `remove_at` - Remove an element at a specific index
-   `get` - Get an element at a specific index
-   `set` - Set an element at a specific index
-   `size` - Get the size of the list
-   `is_empty` - Check if the list is empty
-   `contains` - Check if the list contains an element
-   `index_of` - Get the index of an element
-   `clear` - Clear the list
-   `to_string` - Get a string representation of the list

## Usage

```python
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
```

## Output

```bash
[1, 2, 3, 4, 5]
[1, 2, 4, 5]
False
True
4
4
[1, 2, 4, 5]
         1
         2
         4
         5
```

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

© Copyright Max Base, 2022
