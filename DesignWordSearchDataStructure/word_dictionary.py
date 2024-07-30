# ---------------- Initial Solution ---------------
class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def helper(word, curr):
            if not word:
                return True

            if not curr.children:
                return False
                
            if word[0] == '.':
                if len(word) == 1:
                    for child in curr.children.values():
                        if child.end:
                            return True
                    return False

                found = False
                for child in curr.children.values():
                    found = found or helper(word[1:], child)
                    if found: break
                return found

            if word[0] not in curr.children:
                return False

            curr = curr.children[word[0]]
            return helper(word[1:], curr)

        return helper(word, self.root)


# ----------- Prettier Solution -----------------
class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

