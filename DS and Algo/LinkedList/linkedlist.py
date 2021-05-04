# Each item in the linked list is a node
# Each node is connected to the next node and has a pointer to the next node
# It's unliited meaning there is not end
# In the last node there is no pointer so that is the last node
# The first node is the root node, 

# Operations
    # find(data)
    # add(data)
    # remove(data)
    # print_list(data)

        # add(10) - insert operation
            # we first create a new node with the data 10, 
            # we are going to point the pointer to the root which is the first nodes

        # remove(5)
            # we first need to find the item
            # we do it by starting at the root until we get to the item
            # we take the pointer of the root node and pointing it at the next node of the item we are looking for so that the item is detached from the linked list and is pointing to no nodes
            # the item is now detached from the linked list and is pointing to no nodes - hence deleted

# Attributes
    # Root - pointer to the first node
    # size - number of nodes in the list

 