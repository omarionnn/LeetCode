class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in checker:
                return (i, checker[complement])
            else:
                checker[nums[i]] = i
        