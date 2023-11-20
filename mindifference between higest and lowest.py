class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()  
        left = 0  
        right = k - 1 

        min_diff = nums[right] - nums[left]

        while right < len(nums) - 1:
            left += 1
            right += 1
            diff = nums[right] - nums[left]  
            min_diff = min(min_diff, diff)  

        return min_diff