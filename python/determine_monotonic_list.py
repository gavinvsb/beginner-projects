"""
Given an array of integers, determine whether the array is monotonic or not.
"""

def solution(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 

A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

print(solution(A)) 
print(solution(B)) 
print(solution(C)) 
