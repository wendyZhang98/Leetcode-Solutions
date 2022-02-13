### Description:
<img width="1287" alt="Screen Shot 2022-02-12 at 23 39 15" src="https://user-images.githubusercontent.com/49216429/153738913-708f861d-f1a2-4653-838e-a48409975e1d.png">

### Example:
<img width="1107" alt="Screen Shot 2022-02-12 at 23 39 23" src="https://user-images.githubusercontent.com/49216429/153738917-562fa860-6245-49e7-b531-091fdf67265e.png">


### Solutions:
<img width="1290" alt="Screen Shot 2022-02-12 at 23 45 43" src="https://user-images.githubusercontent.com/49216429/153739075-2d73e422-ed55-4891-b19d-283db9f3005b.png">

<img width="1289" alt="Screen Shot 2022-02-12 at 23 46 28" src="https://user-images.githubusercontent.com/49216429/153739088-3564de94-c5d6-460c-b853-74a8ee7a67a3.png">

<img width="1292" alt="Screen Shot 2022-02-12 at 23 48 05" src="https://user-images.githubusercontent.com/49216429/153739138-e2c44f85-c198-4c33-bc55-1f2a8bfcb086.png">


```
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
```
