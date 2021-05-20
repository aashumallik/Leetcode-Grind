#can't use two for loops
#have to do it in place

#using two pointers

#example = [0,1,0,2]
#result = [1,2,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev_index=0 # we set the second pointer to 0
        for i in range(0,len(nums)): #lopping over nums array
            if nums[i]!=0:#if the first pointer at index i is not equal to 0 - this is when we know to swap the index i with previous index
                hold=nums[prev_index] # we initialize a new varialble that is going to hold the prev index value in this case is 0
                nums[prev_index]=nums[i] #we are going to swap the value at index i with prev index
                nums[i]=hold # we are setting the 0 value at nums i which will move the 0 1 step ahead
                prev_index+=1 # we are moving the prev index 1 place ahead