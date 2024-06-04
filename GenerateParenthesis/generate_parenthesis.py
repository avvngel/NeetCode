#!/usr/bin/env

class Solution:
    """
    Modular Solution
    """
    def is_valid_soln(self, n, state):
        return state[1] == state[2] == n

    def get_candidates(self, n, state):
        candidates = []
        if state[1] < n:
            candidates.append([state[0] + '(', state[1]+1, state[2]])
        if state[2] < state[1]:
            candidates.append([state[0] + ')', state[1], state[2]+1])
        return candidates
        
        
    def search(self, n, state, solns):
        if self.is_valid_soln(n, state):
            solns.append(state[0])
        for candidate in self.get_candidates(n, state):
            self.search(n, candidate, solns)
        

    def generateParenthesis(self, n: int) -> List[str]:
        solns = []
        n_open_pars = 0
        n_closed_pars = 0
        initial_state = ('', n_open_pars, n_closed_pars)
        self.search(n, initial_state, solns)
        return solns

class SimpleSolution:
    """
    Simpler Solution
    """
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        solns = []
        def backtrack(n_open, n_closed):
            if n_open == n_closed == n:
                solns.append(''.join(stack))
                return
            
            if n_open < n:
                stack.append('(')
                backtrack(n_open + 1, n_closed)
                stack.pop()
            
            if n_closed < n_open:
                stack.append(')')
                backtrack(n_open, n_closed + 1)
                stack.pop()
        
        backtrack(0, 0)
        
        return solns



