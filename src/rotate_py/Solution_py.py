from typing import List

class pySolution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        n: int = len(nums)  # Get the length of the list
        k: int = k % n      # Ensure k is within the bounds of the list length

        # Helper function to reverse elements in nums from index 'start' to 'end'
        def reverse(start: int, end: int) -> None:
            while start < end:
                # Swap elements at positions start and end
                nums[start], nums[end] = nums[end], nums[start]
                # Move pointers towards each other
                start, end = start+1, end-1

        reverse(0, n-1)  # Step 1: Reverse the entire list
        reverse(0, k-1)  # Step 2: Reverse the first k elements
        reverse(k, n-1)  # Step 3: Reverse the remaining n-k elements