from typing import List

class pySolution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        # Time Complexity: O(n^2), Space Complexity: O(1)
        # Ensure k is within the bounds of the list length
        # Rotating by the list's length or multiples of it results in the same list
        k = k % len(nums)
        
        # Perform the rotation k times
        for round in range(1, k+1):
            # Store the last element since it will be moved to the front
            lastElement: int = nums[-1]
            
            # Shift all elements one position to the right
            # Start from the end to avoid overwriting values
            for index in range(len(nums)-1, 0, -1):
                nums[index] = nums[index-1]
            
            # Place the previously last element at the beginning
            nums[0] = lastElement