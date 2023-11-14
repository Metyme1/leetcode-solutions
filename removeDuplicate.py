class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_set = set()
        i = 0
        while i < len(nums):
            if nums[i] not in num_set:
                num_set.add(nums[i])
                i += 1
            else:
                nums.pop(i)

        return len(nums)

