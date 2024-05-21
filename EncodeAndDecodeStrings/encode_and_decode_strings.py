#!/usr/bin/env python3

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding_head = chr(len(strs))
        encoding_tail = ''
        for s in strs:
            encoding_head += chr(len(s))
            encoding_tail += s
        return encoding_head + encoding_tail

    def decode(self, s: str) -> List[str]:
        n_strs = ord(s[0])
        word_lengths = []
        decoding = []
        for i in range(1, n_strs+1):
            word_lengths.append(ord(s[i]))

        for length in word_lengths:
            word = ''
            for j in range(length):
                i += 1
                word += s[i]
            decoding.append(word)

        return decoding
