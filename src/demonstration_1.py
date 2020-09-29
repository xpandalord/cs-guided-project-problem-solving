"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""

# assume no duplicates in our `nums` array 
def two_sum(nums, target):
    # Your code here
    # what about using a dictionary? 
    map = {element: index for index, element in enumerate(nums)}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in map:
            return [i, map[diff]]
            
    return "No two elements sum up to the target"

nums = [3, 8, 12, 17]
target = 15
print(two_sum(nums, target))
