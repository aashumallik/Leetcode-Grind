# tuples ()
    # they can be changed once they are created
    # items can not be added once added
    # good for data that are not going to be changed for example gov profiles 
    # all the functions are the same
    # faster than list because 

# create a tuple() - different ways
    # 1) x=()
    # 2) y=(1,3,4)
    # 3) a=1,2,3
    # 4) z=1, # comma tels python that it is a tuple

#converting a list into a tuple
    # list = [2,4]
    # x=tuple(list)
    # print(x)

# trying to delete a tuple
    #  x=(1,2,3)
    #  del(x[1]) - tries to delete item at index 1 but it will fail because you can't change a tuple

# IF YOU HAVE TO CHANGE A TUPLE, the items have to be inside a list
    # x=([1,2],3) - here item at index 1 is a list so that list can be changed
    # del(x[0][0])
    # print(x)