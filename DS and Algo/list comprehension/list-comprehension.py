# practicing list comprehension
# this helps create new list using a for loop or iteration

# basic format
    # new_list=[transform sequence [filter]]

# get values within a range
    # import random
    # under_10=[x for x in range(10)]
    # print('under_10: '+ str(under_10))

# get squared values within a range
    # import random
    # squares = [x**2 for x in under_10]
    # print('squares: ' + str(squares))

# get odd values only from 0 to 9
    # import random
    # odds =  [x for x in range(10) if x%2 == True]
    # print('odds: ' + str(odds))

 # get multiples of 10
    # import random
    # ten_x = [x * 10 for x in range(10)]
    # print('ten_x: ' + str(ten_x))

# get index of a list item
    # names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
    # idx = [k for k, v in enumerate(names) if v == 'Anu']
    # print('index = ' + str(idx[0]))
