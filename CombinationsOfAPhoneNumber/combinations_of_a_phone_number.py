#!/usr/bin/env python3
class Solution:

    dig_to_chars = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        combos = []

        def helper(combo, i):
            nonlocal digits, combos
            
            if i == len(digits):
                combos.append(combo)
                return

            for char in Solution.dig_to_chars[digits[i]]:
                helper(combo + char, i+1)

        if digits: 
            helper('', 0)
            
        return combos

            
