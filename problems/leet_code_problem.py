# my solution 
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         self.nums= nums
#         self.target=target
#         i=0
#         while i<len(self.nums):
#             for v in self.nums:
#                 if(self.nums.index(v)!=i):
#                     if(self.target!=v+self.nums[i]):
#                       continue
#                     else:
#                       li=[]
#                       li.append(self.nums.index(v))
#                       li.append(i)
#                       li.sort()
#                       # print(li)
#                       return li
#                       exit()
                
          
#             i+=1       

            


   

# solution =Solution()
# print(solution.twoSum([3,3],6))
# easymethord

# 1. Two Sum
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}
        print(num_indices)
        print(list(enumerate(nums)))
        for i, num in enumerate(nums):
            print('n',num)
            print(target-num)
            print(i)
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
            print(num_indices)

# Example usage:
solution = Solution()
print(solution.twoSum([2, 4, 5, 6,9,8,7,5], 9))  # Output: [0, 2]

