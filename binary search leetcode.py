# Problem 1: LeetCode Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            # If x is greater, ignore left half
            if nums[mid] < target:
                i = mid + 1

            # If x is smaller, ignore right half
            elif nums[mid] > target:
                j = mid - 1

            # means x is present at mid
            else:
                return mid
        # If we reach here, then the element was not present
        return -1


# Problem 2: Leet Code We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object): 
    
    def guessNumber(self, n):
        i=1
        j=n
        while(j>=i):
            mid=i + (j-i)//2
            pick=guess(mid)
            if pick==0:
                return mid
            if pick==1:
                i=mid+1
            else:
                j=mid-1
    
