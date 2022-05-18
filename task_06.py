def maximum_numb(nums):
    for x in nums:
        if ( nums[0] >= nums[1] ) and ( nums[0] >= nums[2] ):
            return nums[0]
        elif ( nums[1] >= 0 ) and ( nums[1] >= nums [2] ):
            return nums[1]
        elif ( nums[2] >= nums[0] ) and ( nums[2] >= nums[1] ):
            return nums[2]

nums = (45, 786, 41)
print (f'The maximum number is: {maximum_numb(nums)}')