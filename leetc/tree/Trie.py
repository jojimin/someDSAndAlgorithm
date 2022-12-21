class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        def insert_char(char_index, node):
            next_node = node.get(word[char_index])
            if next_node is None:
                next_node = node[word[char_index]] = {}
            if char_index == len(word) - 1:
                next_node["end"] = True
                return
            insert_char(char_index + 1, next_node)

        insert_char(0, self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        def search_char(char_index, node):
            next_node = node.get(word[char_index])
            if next_node is None:
                return False
            else:
                if char_index == len(word) - 1:
                    if next_node.get("end"):
                        return True
                    else:
                        return False
                else:
                    return search_char(char_index + 1, next_node)

        return search_char(0, self.root)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        def search_char(char_index, node):
            next_node = node.get(prefix[char_index])
            if next_node is None:
                return False
            else:
                if char_index == len(prefix) - 1:
                    return True
                else:
                    return search_char(char_index + 1, next_node)

        return search_char(0, self.root)


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
obj.insert("work")
param_2 = obj.search("wor")
param_3 = obj.startsWith("wo")

print(param_2)
print(param_3)


class Trie2:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie2":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie2()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

# obj = Trie2()
# obj.insert("word")
# obj.insert("work")
# param_2 = obj.search("wor")
# param_3 = obj.startsWith("wo")
#
# print(param_2)
# print(param_3)
