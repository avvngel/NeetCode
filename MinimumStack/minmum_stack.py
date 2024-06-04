#!/usr/bin/env python3

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.stack_min:
            min_val = min(val, self.stack_min[-1])
        else:
            min_val = val

        self.stack_min.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


