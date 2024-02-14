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
