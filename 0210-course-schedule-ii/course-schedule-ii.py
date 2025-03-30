class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, preq in prerequisites:
            graph[preq].append(course)
            in_degree[course] += 1
            
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)

        return order if numCourses == len(order) else []
        