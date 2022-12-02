# ArrayList Python

This is a simple implementation of ArrayList in Python.

## Functions

<!-- def __init__(self, size=10):
    self.size = size
    self.count = 0
    self.items = []

def is_empty(self):
    return self.count == 0

def is_full(self):
    return self.count == self.size

def add(self, item):
    if self.is_full():
        raise Exception("List is full")
    self.items.append(item)
    self.count += 1

def add_at(self, index, item):
    if index < 0 or index >= self.size:
        raise Exception("Index out of range")
    self.items.insert(index, item)

def add_first(self, item):
    self.add_at(0, item)

def add_last(self, item):
    self.add(item)

def remove_at(self, index):
    if index < 0 or index >= self.size:
        raise Exception("Index out of range")
    del self.items[index]

def remove_first(self):
    self.remove_at(0)

def remove_last(self):
    self.remove_at(self.count - 1)

def remove(self):
    self.remove_last()

def set(self, index, item):
    if index < 0 or index >= self.size:
        raise Exception("Index out of range")
    if index >= self.count:
        self.count = index + 1
    self[index] = item


def size(self):
    return self.count

def clear(self):
    self.items = []
    self.count = 0

def to_string(self):
    return str(self.items)

def __repr__(self):
    return str(self.items)

def __contains__(self, item):
    return self.contains(item)

def contains(self, item):
    return item in self.items

def index_of(self, item):
    return self.items.index(item)

def __eq__(self, other):
    return self.items == other.items

def __ne__(self, other):
    return self.items != other.items

def __lt__(self, other):
    return self.items < other.items

def __le__(self, other):
    return self.items <= other.items

def __gt__(self, other):
    return self.items > other.items

def __ge__(self, other):
    return self.items >= other.items

def __add__(self, other):
    return self.items + other.items

def __iadd__(self, other):
    self.items += other.items
    return self

def __isub__(self, other):
    self.items -= other.items
    return self

def __sub__(self, other):
    return self.items - other.items

def __mul__(self, other):
    return self.items * other

def __imul__(self, other):
    self.items *= other
    return self

def __rmul__(self, other):
    return self.items * other

def get(self, index):
    if index < 0 or index >= self.count:
        raise Exception("Index out of range")
    return self.items[index]

def __str__(self):
    return str(self.items)

def __len__(self):
    return len(self.items)

def __iter__(self):
    return iter(self.items)

def __getitem__(self, index):
    return self.get(index)

def __setitem__(self, index, value):
    if index < 0 or index >= self.size:
        raise Exception("Index out of range")
    self.items[index] = value

def __delitem__(self, index):
    del self.items[index] -->

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
