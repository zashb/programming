"""
comp: O(m) for insert, search, starts_with; m=key length
applications: autocomplete, spell checker, IP routing, T9, solving word games
"""


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
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
