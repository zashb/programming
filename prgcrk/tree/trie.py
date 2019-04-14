class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    def starts_with(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


# from collections import defaultdict
#
#
# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.is_word = False
#
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         current = self.root
#         for char in word:
#             current = current.children[char]
#         current.is_word = True
#
#     def search(self, word):
#         current = self.root
#         for char in word:
#             if not current:
#                 return False
#             current = current.children.get(char)
#         return current.is_word
#
#     def starts_with(self, prefix):
#         current = self.root
#         for char in prefix:
#             if not current:
#                 return False
#             current = current.children.get(char)
#         return True
#
#
trie = Trie()
trie.insert("apple")

actual = trie.search("apple")
expected = True
print(expected == actual)

actual = trie.search("app")
expected = False
print(expected == actual)

actual = trie.starts_with("app")
expected = True
print(expected == actual)

actual = trie.starts_with("ppa")
expected = False
print(expected == actual)

trie.insert("app")

actual = trie.search("app")
expected = True
print(expected == actual)
