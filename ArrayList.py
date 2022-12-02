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
    
    def insert(self, item):
        if self.is_full():
            raise Exception("List is full")
        self.items.append(item)
        self.count += 1
    
    def remove(self, item):
        if self.is_empty():
            raise Exception("List is empty")
        self.items.remove(item)
        self.count -= 1
    
    def search(self, item):
        return item in self.items
    
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
