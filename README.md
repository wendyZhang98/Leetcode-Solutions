# Leetcode-Practice

This repo consists of problems and answers related to algorithm and data structuer from leetcode. 

Useful Reference: \
💙动态规划的意义：https://www.zhihu.com/question/23995189/answer/613096905 \
💙动态规划之背包问题：https://zhuanlan.zhihu.com/p/93857890 \
💙动态规划三大步骤+案例讲解：https://zhuanlan.zhihu.com/p/91582909 \
💙递推&贪心&搜索&动态规划：https://www.zhihu.com/question/23995189/answer/35429905

🖤回溯：https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3%E4%BF%AE%E8%AE%A2%E7%89%88.md 

Algorithm Basics: \
🧡Tutorialspoint: https://www.tutorialspoint.com/data_structures_algorithms/algorithms_basics.htm \
🧡GeeksForGeeks: https://www.geeksforgeeks.org/fundamentals-of-algorithms/#SearchingandSorting \
🧡Fucking-Algorithms: https://github.com/labuladong/fucking-algorithm \
🧡Algorithm Base：https://github.com/chefyuan/algorithm-base 


To Do List: \
🟢https://github.com/keon/algorithms \
🟢https://github.com/Jack-Lee-Hiter/AlgorithmsByPython 

💚String: https://www.geeksforgeeks.org/string-data-structure/ \
💚Array: https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/ \
💚Binary Tree: https://medium.com/techie-delight/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f \
💚Linked List: https://www.geeksforgeeks.org/top-20-linked-list-interview-question/ \
💚Stack & Queue: https://www.geeksforgeeks.org/stack-data-structure/ 

💚Sorting: https://www.geeksforgeeks.org/sorting-algorithms/ \
💚Backtracking: https://www.geeksforgeeks.org/top-20-backtracking-algorithm-interview-questions/ \
💚Dynamic Programming: https://www.geeksforgeeks.org/top-20-dynamic-programming-interview-questions/ 


# 回溯问题：
## 算法思路：
解决一个回溯问题，实际上就是一个决策树的遍历过程。\
你只需要思考 3 个问题：\
1、路径：已经做出的选择。\
2、选择列表：你当前可以做的选择。\
3、结束条件：到达决策树底层，无法再做选择的条件。

## 算法框架：
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
