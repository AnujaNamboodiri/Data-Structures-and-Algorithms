def binarySearch(nums, target):
    
    i = 0
    j = len(nums)-1
    while i < j:
        mid = i + (j-i) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1
    return -1
        
           

## Driver Code
nums = [2,6,10,52,64,87,99]
target = 10
result = binarySearch(nums, target) 