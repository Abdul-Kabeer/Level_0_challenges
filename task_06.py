#This will print out the maximum number of three digits provided.
def maximum_number(nums):
    if ( nums[0] >= nums[1] ) and ( nums[0] >= nums[2] ):
        largest = nums[0]
    if ( nums[1] >= 0 ) and ( nums[1] >= nums [2] ):
        largest = nums[1]
    if ( nums[2] >= nums[0] ) and ( nums[2] >= nums[1] ):
        largest = nums[2]
    return largest

nums = [65, 12, 41]
print (f'The maximum number is: {maximum_number(nums)}')