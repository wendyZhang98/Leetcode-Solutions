# https://leetcode.com/problems/word-break-ii/



### Description:
# Given a string s and a dictionary of strings wordDict, 
# add spaces in s to construct a sentence where each word is a valid dictionary word. 
# Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.





### Examples:
# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]

# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []




### Solution:
# The solutions for this problem go by many names, 
# such as 🎖Dynamic Programming, 🎖recursion with memoization, 🎖DFS, and 🎖backtracking etc. 
# They all capture certain traits of the solutions.
# In essence, all these solutions can all be categorized as variants of Dynamic Programming (DP), as we will discuss in this article.

# As a reminder, with DP, 
# we break the original problem down to several sub-problems recursively until the sub-problems are small enough to be solved directly. 
# Then we combine the results of sub-problems to obtain the final solution for the original problem.

# As one can see, the DP solutions are also the embodiment of the divide-and-conquer principle.
# To come up a DP solution, the essential step is to represent the solution of the original problem with the results of its sub-problems. 
# In general, there are two approaches to implement a DP solution, namely 🎖Top-Down and 🎖Bottom-Up. 
# We would explain in detail how to apply these two approaches to this problem in the following sections. 


### 🧩Approach 1: Top-Down Dynamic Programming🧩
# For any word (denoted as w) in the dictionary, 
# if it matches with a prefix of the input string, we then can divide the string into two parts: 
# the word and the postfix, i.e. s=w+postfix.

# For example, the word cat matches with a prefix of the string. As a result, we can divide the string into s=‘cat’+‘sanddog’.
# The above approach can be considered as a top-down DP. 
# The reason lies in the part that we adopt the laissez-faire strategy, 
# i.e. we simply take a first step, while assuming the subsequent steps will figure out on their owns.

# Each node in the graph represents a postfix of the input string. 
# In particular, we have some nodes with an empty string, which indicates the end of the input string. 
# Each edge indicates the reduction from one postfix to another. 
# The label on top of each edge indicates the word that is used to trigger the reduction.


class Solution:
    def wordBreak(self, s, wordDict]):
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        #@lru_cache(maxsize=None)    # alternative memoization solution
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]

      
      
### Approach 2: Bottom-Up Dynamic Programming

class Solution:
    def wordBreak(self, s, wordDict):
        # quick check on the characters,
        # otherwise it would exceed the time limit for certain test cases.
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []

        wordSet = set(wordDict)

        dp = [[]] * (len(s)+1)
        dp[0] = [""]

        for endIndex in range(1, len(s)+1):
            sublist = []
            # fill up the values in the dp array.
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        sublist.append((subsentence + ' ' + word).strip())

            dp[endIndex] = sublist

        return dp[len(s)]

