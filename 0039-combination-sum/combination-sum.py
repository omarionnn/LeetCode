class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(i, path, target):
            if target == 0:
                res.append(path[:])
                return 
            if target < 0:
                return 

            for i in range(i, len(candidates)):
                curr = candidates[i]
                path.append(curr)

                backtrack(i, path, target - curr)

                path.pop()
        res = []
        candidates.sort()
        backtrack(0, [], target)
        return res
        