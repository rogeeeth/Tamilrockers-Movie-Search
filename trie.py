class Trie:
    
    def __init__(self):
        self.end = False
        self.child = [None]*26
        
    def insert(self,s):
        t =self
        for c in s:
            if t.child[ord(c)-ord('a')]==None:
                t.child[ord(c)-ord('a')] =Trie()
            t = t.child[ord(c)-ord('a')]
        t.end = True
        
    def search(self, s):
        t = self
        for c in s:
            if t.child[ord(c)-ord('a')]==None: return False
            t = t.child[ord(c)-ord('a')]
            if t.end: return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = collections.deque()
        for w in words:
            self.trie.insert(reversed(w))
            
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
