#  n2 solution


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            for j in range(i):
                if nums[i] + nums[j] < target:
                    count += 1
        return count


#  linear solution


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left  # Add all pairs between left and right
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left if the sum is too big

        return count
