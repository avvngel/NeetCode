#!/usr/bin/env python3

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        count = n

        for n1, n2 in edges:
            if parents[n1] == parents[n2]:
                count += 1
            parents[n2] = parents[n1]
            count -= 1

        return count

    def countComponents_DFS(self, n: int, edges: List[List[int]]) -> int:
    """
    DFS Solution
    """
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        left_to_visit = set(range(n))
        def dfs(curr, prev):
            if curr not in left_to_visit:
                return

            left_to_visit.remove(curr)
            for next in adj[curr]:
                if next == prev:
                    continue
                dfs(next, curr)
        count = 0
        while left_to_visit:
            dfs(next(iter(left_to_visit)), -1)
            count += 1
            
        return count
        
                
