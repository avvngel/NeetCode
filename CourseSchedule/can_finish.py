#!/usr/bin/env python3

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        visited = set()
        course_to_prereq = defaultdict(list)
        
        for i, j in prerequisites:
            course_to_prereq[i].append(j)
        
        def has_cycle(a):
            nonlocal visited

            if a in visited:
                return True

            visited.add(a)
            for b in course_to_prereq[a]:
                if has_cycle(b):
                    return True
            visited.remove(a)

            course_to_prereq[a] = []
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True
