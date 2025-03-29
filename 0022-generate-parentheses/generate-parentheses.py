class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(path, open, close):
            if len(path) == 2 * n:
                res.append(path[:])
                return 

            if open < n:
                dfs(path + '(', open + 1, close)

            if close < open:
                dfs(path + ')', open, close + 1)


        res = []
        dfs("", 0, 0)
        return res
        