# Max heaps is fast
    # Insert an item in 0(log n)
    # Get Max 0(1)
    # Remove Max in 0(log n)

# Easy to implement using a list -  not as easy as queue or stacks but easy enough
    # If you need an item in Max Heap - Get the index
    # If you need an item's parent - Index/2
    # If you need an item's children - Index*2 to get let child and Index*2+1 for the right child

# Operations
    # Push (insert) - Implementation
        # Add a value to end of the array 
        # Float it up to it's proper position (If it's lower than the parent value, swap it up to the parent place. keep comparing until value reaches desired place)
    # Pop (remove max)
        # Move max to end end of the array
        # Delete the max value
        # Swap down the item to it's proper position by comparing value
        # Return the Max value
    # Peek (get max)
        # Return the Max value

# A MaxHeap always bubbles the highest value to the top, so it can be removed instantly.
# Public functions: push, peek, pop
# Private functions: swap, floatUp, bubbleDown, str__.

class MaxHeap:
    # Constructor - we have to pass a list always
    def __init__(self, items=[]):
        super().__init__()
        # We always insert a 0 for index 0 because Max heap starts at 1
        self.heap = [0]
        for item in items:
            # Add them one at a time to the end of the list
            self.heap.append(item)
            # float it up to it's proper position
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        # Appends the data to the end of the heap
        self.heap.append(data)
        # float it up to it's proper position
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        # returns the top item in the heap
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
            
    def pop(self):
        # if there are more than 2 items, we are going to swap the first item with the last item 
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            # we pop off the last item and assign it to the vairable max
            max = self.heap.pop()
            self.__bubbleDown(1)
        # if the list has 2 items, then the heap only have 1 real item because the first item is always a 0 at index 0 - look at line 31 for more explanation
        elif len(self.heap) == 2:
        # Pop of the 1 item at index 1
            max = self.heap.pop()
        else: 
            max = False
        return max

# Utility functions
 
    def __swap(self, i, j):
        # swaps two items, we pass to indexes and swap those two indexes
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# float up receives an index in the constructor
    def __floatUp(self, index):
        # we get the parent's index
        parent = index//2
        # if it's already at the top there's no need to get the parent
        if index <= 1:
            return
        # we are going to compare with it's parent, it it's greater than the parent , swap the position
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            # we are calling the floatup function recursively until the item reaches it's position
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
            
    def __str__(self):
        return str(self.heap)

# TEST CODE
m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())