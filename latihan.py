from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        graph = defaultdict(list)
        level = {beginWord}
        found = False
        visited = set()
        
        while level and not found:
            next_level = set()
            visited |= level
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordSet and next_word not in visited:
                            if next_word == endWord:
                                found = True
                            next_level.add(next_word)
                            graph[next_word].append(word)
            level = next_level

        if not found:
            return []

        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for prev in graph[word]:
                backtrack(prev, path + [prev])

        backtrack(endWord, [endWord])
        return res
