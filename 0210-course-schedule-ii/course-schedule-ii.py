class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            in_degree[crs] += 1

        q = (deque(i for i in range(numCourses) if in_degree[i] == 0))

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for c in graph[course]:
                in_degree[c] -= 1

                if in_degree[c] == 0:
                    q.append(c)

        return order if len(order) == numCourses else []
        