#!/usr/bin/env python3

def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairings = {'(': ')',
                            '{': '}',
                            '[': ']'}
        for char in s:
            if char in bracket_pairings:
                stack.append(char)
            else:

                if not stack or bracket_pairings[stack[-1]] != char:
                    return False
                stack.pop()

        return not stack
