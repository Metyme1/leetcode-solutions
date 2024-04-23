class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        r = 0
        w = 1
        while w < len(nums):
            if nums[r] == nums[w]:
                nums[r] = 2 * nums[r]
                nums[w] = 0
                r += 2
                w += 2
            else:
                r += 1
                w += 1
        r1 = 0
        w1 = 0
        while r1 < len(nums):
            if nums[r1] != 0:
                temp = nums[r1]
                nums[r1] = nums[w1]
                nums[w1] = temp

                w1 += 1
            r1 += 1
        return nums
