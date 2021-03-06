# Problem 1
# Solution 1 - Brute Force - Double for loop solution , O(n^2)
# Solution 2 -optimized soln - Using a Hash Map or Dictionary

## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## You can return the answer in any order.

## Example 1:
## Input: nums = [2,7,11,15], target = 9
## Output: [0,1]
## Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return([i,j])

# Using a Dictionary or a hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # dictionary to store key index and value
        for i, num in enumerate(nums): #enumerate gives index and the value both at once
            if target - num in seen:
                return([seen[target-num],i])
            elif num not in seen:
                seen[num]=i



        