#!/usr/bin/env python3

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict

        if not edges: 
            return True
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)
            for next in adj[curr]:
                if next == prev:
                    continue
                if not dfs(next, curr):
                    return False
            return True
        
        return dfs(edges[0][0], -1) and len(visited) == n

