#  Problem 1 : Look for a particular element in an array and return the index if found
#  Time complexity = O(n) searching algorithm is 'Linear Search' (worst case scenario)

def linearSearch(arr, search_element, n):
	for i in range(n):
		if arr[i] == search_element:
			return i
            # Element is not present inside the array
	
	return -1
    # Element is not present inside the array

## Driver Code
arr = [53, 12, 32, 17, 30,19]
search_element = 93     ## Try different values to test the code
n = len(arr)
result = linearSearch(arr,search_element, n)
print("Search element results is:", result)

## Done

# Problem 2: Binary Search using Recursive Technique
# Time complexity - O(logn) 

def binarySearch(array, i, j, x):
	## Single element problem
	## For small problems time complexity : O(1) --> constant time complexity
	if i == j:
		if array[i] == x:
			return i
		else:
			return -1
	## Multi-element problem
	else:
		mid = i + (j-i) // 2		# constant
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			## Recursive call
			return binarySearch(array, mid+1, j, x)			
		else:
			## Recursive call
			return binarySearch(array, i, mid-1, x)			

## Driver Code
array = [ 5, 10, 20, 27, 30, 35, 39, 42]
i = 0
j = len(array) - 1
x = 39
result = binarySearch(array, i, j, x)
print("Searching value is present at index:", result)

# Problem 3 : Binary Search using Iterative Approach
# Time complexity O(1)

def binarySearch(array, x):
	i = 0
	j = len(array) - 1
	while i < j:
		mid = i + (j-1) // 2
		
		# If x is greater, ignore left half
		if array[mid] < x:
			i = mid + 1

		# If x is smaller, ignore right half
		elif array[mid] > x:
			j = mid - 1
		
		# means x is present at mid
		else:
			return mid
	# If we reach here, then the element was not present
	return -1

## Driver Code
array = [ 5, 10, 20, 27, 30, 35, 39, 42]
x = 10
result = binarySearch(array, x)
print("Searching value is present at index:", result)

