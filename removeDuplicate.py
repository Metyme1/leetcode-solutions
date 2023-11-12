from ast import List


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

# Example usage:
sol = Solution()
nums = [1, 1, 2]
result = sol.removeDuplicates(nums)
print(result)  # It should print 2
print(nums)    # It should print [1, 2, _]
