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

# 动态规划
## 算法思路
- 将一个问题拆成几个子问题，分别求解这些子问题，即可推断出大问题的解
1. 无后效性: 如果给定某一阶段的状态，则在这一阶段以后过程的发展不受这阶段以前各段状态的影响 \
2. 最优子结构：大问题的最优解可以由小问题的最优解推出 \

# 回溯问题
## 算法思路
解决一个回溯问题，实际上就是一个决策树的遍历过程。\
你只需要思考 3 个问题：\
1、路径：已经做出的选择。\
2、选择列表：你当前可以做的选择。\
3、结束条件：到达决策树底层，无法再做选择的条件。

## 算法框架
<img width="926" alt="Screen Shot 2021-10-08 at 7 42 31 PM" src="https://user-images.githubusercontent.com/49216429/136635062-2082ab82-cbba-45dc-99b5-a550892f77f6.png">
- 其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」
- 写 backtrack 函数时，需要维护走过的「路径」和当前可以做的「选择列表」，当触发「结束条件」时，将「路径」记入结果集

## 算法习题
- 全排列
- N 皇后
