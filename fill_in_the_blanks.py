"""
Given an array containing None values fill in the None values with most recent non None value in the array.
"""

def solution(array):
    valid = 0            
    res = []                 
    for i in nums: 
        if i is not None:    
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

array1 = [1,None,2,3,None,None,5,None]

solution(array1)
