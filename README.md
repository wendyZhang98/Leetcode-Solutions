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

<img width="850" alt="Screen Shot 2021-10-08 at 10 10 33 PM" src="https://user-images.githubusercontent.com/49216429/136640272-21dfec2d-b416-41a9-9b25-b8f01bb0f2b9.png">

# 排序
### 冒泡排序
- 交换排序算法（小的元素通过交换慢慢“冒泡”到数列的顶端）
- 重复走访需要排序的数列，一次比较两个元素，如果顺序错误就将它们调换过来
- 重复操作直到数列排序完成
- 思路简单、代码简单、适合数据量较小时候的排序；算法复杂度较高，在数据量较大时不适用

### 选择排序
- 交换排序算法（冒泡排序的改进）
- 在未排序序列中寻找最小/大元素，存放到排序序列的起始位置
- 从剩余未排序元素中继续操作直到数列排序完成

### 插入排序
- 把需要排序的数组分为已排序&未排序两部分
- 从第二个元素开始，在已经排好序的子数组中寻找该元素合适的位置并且插入

### 归并排序


### 快速排序
- 从数列中挑出一个元素，称为基准（pivot）
- 重新排序数列，所有比基准值小的元素摆放在基准前面，反之亦然（相同的数可以放在任意一边）
- 在这个分区结束之后，该基准值处于数列的中间位置，此操作成为分区（partition）
- 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子序列排序

### 堆排序

### 希尔排序

### 桶排序

### 基数排序


# 二叉树
### 遍历二叉树
- 先序遍历：根——>左——>右
- 中序遍历：左——>根——>右
- 后序遍历：左——>右——>根
- 层序遍历：第n层——>第n+1层

# 二分搜索树（BST）



# 动态规划
## 算法思路
- 动态规划（Dynamic Programming/DP）是运筹学一个分支。其把多阶段问题变换为一系列相互联系的单阶段问题，逐个加以解决
- 动态规划是解决多阶段决策过程最优化的一种数学方法；不是某种具有固定范式的特殊算法；是一种道而不是一种术，难在即使学会了这种思想，也要具体问题具体分析
- DP核心思想：尽量缩小解空间
- 动态规划特点：1. 无后效性（马尔科夫性）: 如果给定某一阶段的状态，则在这一阶段以后过程的发展不受这阶段以前各段状态的影响。2. 最优子结构：大问题的最优解可以由小问题的最优解推出 



## 算法设计：
1. 设计状态
2. 设计状态转移方程（从哪里来/到哪里去）

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
