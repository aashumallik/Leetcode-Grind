#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#Example 1:
#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4

# Solution 1 - Brute Force - Double for loop solution , O(n^2)
# Solution 2 -optimized soln - Using a Hash Map or Dictionary

# Brute Force
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num==target:
                return i
        return -1

# Optimal solution
# Nums = [-1,3,4,6,8,9,12,15,18] Target = 9
# start_index = 0
# end_index = 8
# middle_index = (start_index+end_index) / 2 
# middle_index = 4

# start = 4
# end = 8
# mid = 6

# start = 4
# end = 6
# mid = 5 return 9 at index 5

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        while start <= end:
            middle = (start + end) // 2
            num = nums[middle]
            if target == num:
                return middle

            if target > num:
                start = middle + 1

            if target < num:
                end = middle - 1

        return -1

        