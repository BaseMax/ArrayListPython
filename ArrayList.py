#
# @Author: Max Base
# @Name: ArrayList Python
# @Repository: https://github.com/BaseMax/ArrayListPython
# @Date: 2022-12-02
#

class ArrayList:
    def __init__(self, size=10):
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
        del self.items[index]
