class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        state = {}
        max_fruit = 0
        startAnxious = 0

        #state = {1: 2, 2: 1}

        for endAvoidant in range(len(fruits)):
            state[fruits[endAvoidant]] = state.get(fruits[endAvoidant], 0) + 1

            while len(state) > 2:
                state[fruits[startAnxious]] -= 1
                if state[fruits[startAnxious]] == 0:
                    del state[fruits[startAnxious]]
                startAnxious += 1

            max_fruit = max(max_fruit, endAvoidant - startAnxious + 1)

        return max_fruit

        