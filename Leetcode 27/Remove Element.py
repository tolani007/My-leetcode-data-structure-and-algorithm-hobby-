class Solution(object):
    def removeElement(self, nums, val):
         n = len(nums)
         write_pos = 0
         if n == 0:
            return 0
         for scan_pos in range(n):
            if nums[scan_pos]!= val:
                nums[write_pos] = nums[scan_pos]
                write_pos += 1
         return write_pos
