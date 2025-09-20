[Remove Duplicates from Sorted Array on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Intuition
Because nums is sorted, duplicates will always be right next to each other. I never have to search forward or backward beyond immediate neighbors to check for duplication.

I want to build a “prefix” of unique values at the front of the array, overwriting the duplicates as I go.

Use a pointer k (or “write position”) to track how many unique values I’ve kept so far. Every time I find a new value (one that differs from the last unique), write it at nums[k], then bump k.

Approach
Initialize k = 0 — this will be where I place the next unique value and also represents how many uniques I have seen (since first unique will fill at index 0).

I loop through every element number in nums:

If k == 0, this is the first element; it’s unique by default.

Or if number != nums[k-1], it’s different from the last unique you wrote → a new unique.

When it’s a new unique, set nums[k] = number, then k += 1.

If it’s a duplicate (equal to nums[k-1]), skip it.

After the full loop, k is count of unique elements; the first k positions of nums are the unique ones, in sorted order. Return k.

Complexity
Time complexity:
O(n), where 𝑛 is the length of nums. You walk through the array exactly once, doing constant work per element.

Space complexity:
O(1) extra space. You only use a few variables (k, loop variable, etc.). You modify the input array in place. No large auxiliary structures.


Code snippet:
<img width="1148" height="486" alt="image" src="https://github.com/user-attachments/assets/811bdc17-4e0b-4c55-97e7-5de1acf95d5a" />
