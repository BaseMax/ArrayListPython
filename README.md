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

And a couple of magic methods:

-   `__str__` - Get a string representation of the list
-   `__repr__` - Get a string representation of the list
-   `__len__` - Get the size of the list
-   `__iter__` - Get an iterator for the list
-   `__getitem__` - Get an element at a specific index
-   `__setitem__` - Set an element at a specific index
-   `__delitem__` - Remove an element at a specific index
-   `__add__` - Add two lists together
-   `__iadd__` - Add two lists together
-   `__sub__` - Subtract two lists
-   `__isub__` - Subtract two lists
-   `__mul__` - Multiply a list by a number
-   `__imul__` - Multiply a list by a number
-   `__rmul__` - Multiply a list by a number
-   `__eq__` - Check if two lists are equal
-   `__ne__` - Check if two lists are not equal
-   `__lt__` - Check if one list is less than another
-   `__le__` - Check if one list is less than or equal to another
-   `__gt__` - Check if one list is greater than another
-   `__ge__` - Check if one list is greater than or equal to another

## Usage

```python
from ArrayList import ArrayList

# Create a new list
list = ArrayList(10)

# Add items to the list
list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add(5)

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
