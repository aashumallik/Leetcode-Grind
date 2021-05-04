
# Imagine a stack of books
# LIFO -Last in first out
# Push - Push an item to the top of the stack
# Append - Push an item to the top of the stack
# Pop - Pop an item off the stack
# Commads executed in a computer is done using a stack

# Implementation
    # my_stack=list()
    # my_stack.append(1)
    # my_stack.append(4)
    # print(my_stack)
    # my_stack.pop(1)
    # print(my_stack)


# Stack using List with a Wrapper Class
    # We create a Stack class and a full set of Stack methods.
    # But the underlying data structure is really a Python List.
    # For pop and peek methods we first check whether the stack is empty, to avoid exceptions.

        # class Stack():
        #     def __init__(self):
        #         self.stack = list()
        #     def push(self, item):
        #         self.stack.append(item)
        #     def pop(self):
        #         if len(self.stack) > 0:
        #            return self.stack.pop()
        #         else:
        #             return None
        #     def peek(self):
        #         if len(self.stack) > 0:
        #             return self.stack[len(self.stack)-1]
        #         else:
        #             return None
        #     def __str__(self):
        #         return str(self.stack)

    # Test Code for Stack Wrapper Class

        # my_stack = Stack()
        # my_stack.push(1)
        # my_stack.push(3)
        # print(my_stack)
        # print(my_stack.pop())
        # print(my_stack.peek())
        # print(my_stack.pop())
        # print(my_stack.pop())



