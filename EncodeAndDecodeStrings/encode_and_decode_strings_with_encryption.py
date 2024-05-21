class Solution:    

    def encode(self, strs: List[str]) -> str:
        encoding_head = chr(len(strs))
        encoding_tail = ''
        for s in strs:
            encoding_head += chr(len(s))
            for char in s:
                encoding_tail += chr(ord(char)-12)
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
                word += chr(ord(s[i])+12)
            decoding.append(word)

        return decoding



