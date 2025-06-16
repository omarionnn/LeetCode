class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0

        l = 0

        for r in range(1, len(nums)):
            if nums[l] > nums[r]:
                l = r
            else:
                res = max(res, nums[r] - nums[l])

        if res == 0:
            return -1
        else:
            return res
        