class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(j , root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == ".":
                    for k in curr.children.values():
                        if dfs(i+1, k):
                            return True
                    return False        
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.word
        return dfs(0, self.root)
