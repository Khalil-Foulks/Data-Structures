"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# # Using an array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()
#         return None

# Using a Linked List
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __str__(self):
        return f'{self.size} : {self.storage}'

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        return None

# testing_list = Stack()
# print(testing_list, "Empty")
# testing_list.push(100)
# print(testing_list.__len__, "length")
# print(testing_list, "First add")
# testing_list.push(101)
# print(testing_list.__len__, "length")
# print(testing_list, "Second add")
# testing_list.push(105)
# print(testing_list.__len__, "length")
# print(testing_list, "third add")
# testing_list.pop()
# print(testing_list.__len__, "length")
# print(testing_list, "pop 1")
# testing_list.pop()
# print(testing_list.__len__, "length")
# print(testing_list, "pop 2")
# testing_list.pop()
# print(testing_list.__len__, "length")
# print(testing_list, "pop 3")
# print(testing_list, "list")