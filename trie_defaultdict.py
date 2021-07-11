import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        self.children[char]


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Add word to trie
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, word):
        # Check if word exists in trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word
