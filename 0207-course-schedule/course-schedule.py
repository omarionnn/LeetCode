class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, preq in prerequisites:
            graph[preq].append(course)
            in_degree[course] += 1
            
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_taken = 0

        while queue:
            course = queue.popleft()
            courses_taken += 1

            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)

        return courses_taken == numCourses