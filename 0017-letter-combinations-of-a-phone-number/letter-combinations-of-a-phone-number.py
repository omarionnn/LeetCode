class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

        res = []

        def dfs(path, idx):
            if idx == len(digits):
                res.append(path)
                return 

            for letter in phone[digits[idx]]:
                dfs(path + letter, idx + 1)

        if digits:
            dfs("", 0)
            return res
        else:
            return []

    
        