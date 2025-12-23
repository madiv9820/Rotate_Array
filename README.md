# [Rotate Array](https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

### Problem
Given an integer array $nums$, rotate the array to the right by $k$ steps, where $k$ is non-negative.

### Examples
- Input: `nums = [1,2,3,4,5,6,7]`, `k = 3` <br>
Output: `[5,6,7,1,2,3,4]`
 
- Input: `nums = [-1,-100,3,99]`, `k = 2` <br>
Output: `[3,99,-1,-100]`

### Constraints
- $1 <= nums.length <= 10^5$
- $-2^{31} <= nums[i] <= 2^{31} - 1$
- $0 <= k <= 10^5$
---

### Approaches
- ### [**Shifting Elements**](https://github.com/madiv9820/Rotate_Array/tree/Approach_01-Shifting_Elements)
    
    Rotates a list to the right by `k` steps by repeatedly moving the last element to the front. Modifies the list **in-place** with **O(1) extra space**, but has a **time complexity of O(n × k)**, making it inefficient for large `k` or long lists.

- ### [**Reverse Subarrays**](https://github.com/madiv9820/Rotate_Array/tree/Approach_02-Reverse_Subarrays)

    Rotates a list to the right by `k` steps using the **three-step reversal method**. This approach performs the rotation **in-place** with **O(1) extra space** and runs in **O(n) time**, making it efficient for large lists.
---
