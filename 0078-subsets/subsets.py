class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(path, idx):
            if idx == len(nums):
                res.append(path[:])
                return 

            path.append(nums[idx])
            dfs(path, idx + 1)

            path.pop()
            dfs(path, idx + 1)


        res = []
        dfs([], 0)
        return res
        