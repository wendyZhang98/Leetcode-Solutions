### 🎖Leetcode-Practice
This repository consists of my practice of algorithm & data structures since 2020.


### 🎖Practice of [TwoPointers]:
- [Reverse Vowels of a String](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/String/%5BTwoPointers%5DReverse_Vowels_of_a_String.md)
- [Container With Most Water](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/Array/%E2%9C%85%5BTwoPointers%5DContainer%20With%20Most%20Water.md)
- [Merge Sorted Array](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/Array/%E2%9C%85%5BTwoPointers%5DMerge%20Sorted%20Array.md)
- [Move Zeros](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/Array/%E2%9C%85%5BTwoPointers%5DMove%20Zeros.md)
- [Remove Element](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/Array/%E2%9C%85%5BTwoPointers%5DRemove%20Element.md)
- [Squares of a Sorted Array](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/Array/%E2%9C%85%5BTwoPointers%5DSquares%20of%20a%20Sorted%20Array.md)


### 🎖Practice of [SlidingWindows]:
- [Longest Substring Without Repeating Characters](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/String/%5BSlidingWindow%5DLongest_Substring_Without_Repeating_Characters.md) 

### 🎖Practice of [DynamicProgramming]:
- [Longest Palindromic Substring](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/String/%5BDynamicProgramming%5DLongest_Palindromic_Substring.md)

### 🎖Practice of [Divide&Conquer]:
- [Longest Common Prefix](https://github.com/wendyZhang98/Leetcode-Practice/blob/master/String/%5BDivide%26Conquer%5DLongest_Common_Prefix.md)


<img width="850" alt="Screen Shot 2021-10-08 at 10 10 33 PM" src="https://user-images.githubusercontent.com/49216429/136640272-21dfec2d-b416-41a9-9b25-b8f01bb0f2b9.png">

### 🎖算法讲解 Reference：
- [十大排序](https://leetcode.cn/circle/discuss/eBo9UB/)

### 🎖刷题指南:
- [花花酱](https://zxi.mytechroad.com/blog/leetcode-problem-categories/) 


### 🎖排序算法之冒泡排序
- 交换排序算法（小的元素通过交换慢慢“冒泡”到数列的顶端）
- 重复走访需要排序的数列，一次比较两个元素，如果顺序错误就将它们调换过来
- 重复操作直到数列排序完成
- 思路简单、代码简单、适合数据量较小时候的排序；算法复杂度较高，在数据量较大时不适用

### 🎖排序算法之选择排序
- 交换排序算法（冒泡排序的改进）
- 在未排序序列中寻找最小/大元素，存放到排序序列的起始位置
- 从剩余未排序元素中继续操作直到数列排序完成

### 🎖排序算法之插入排序
- 在插入排序中，我们从前到后依次处理未排好序的元素
- 对于每个元素，我们将它与之前排好序的元素进行比较，找到合适的位置然后插入

### 🎖排序算法之归并排序
- 将一个数组分为两个数组，通过递归重复将数组切分到只剩下一个元素为止
- 然后将每个子数组中的元素排序后合并，通过不断合并子数组得到排序完成的数组

### 🎖排序算法之快速排序
- 从数列中挑出一个元素，称为基准（pivot）
- 重新排序数列，所有比基准值小的元素摆放在基准前面，反之亦然（相同的数可以放在任意一边）
- 在这个分区结束之后，该基准值处于数列的中间位置，此操作成为分区（partition）
- 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子序列排序

### 🎖遍历二叉树
- 先序遍历：根——>左——>右
- 中序遍历：左——>根——>右
- 后序遍历：左——>右——>根
- 层序遍历：第n层——>第n+1层

### 🎖动态规划算法思路
- 动态规划（Dynamic Programming/DP）是运筹学一个分支。其把多阶段问题变换为一系列相互联系的单阶段问题，逐个加以解决
- 动态规划是解决多阶段决策过程最优化的一种数学方法；不是某种具有固定范式的特殊算法；是一种道而不是一种术，难在即使学会了这种思想，也要具体问题具体分析
- DP核心思想：尽量缩小解空间
- 动态规划特点：1. 无后效性（马尔科夫性）: 如果给定某一阶段的状态，则在这一阶段以后过程的发展不受这阶段以前各段状态的影响。2. 最优子结构：大问题的最优解可以由小问题的最优解推出 

### 🎖动态规划算法设计：
1. 设计状态
2. 设计状态转移方程（从哪里来/到哪里去）

### 🎖回溯问题算法思路
解决一个回溯问题，实际上就是一个决策树的遍历过程。\
你只需要思考 3 个问题：\
1、路径：已经做出的选择。\
2、选择列表：你当前可以做的选择。\
3、结束条件：到达决策树底层，无法再做选择的条件。

### 🎖回溯问题算法框架
<img width="926" alt="Screen Shot 2021-10-08 at 7 42 31 PM" src="https://user-images.githubusercontent.com/49216429/136635062-2082ab82-cbba-45dc-99b5-a550892f77f6.png">

- 其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」
- 写 backtrack 函数时，需要维护走过的「路径」和当前可以做的「选择列表」，当触发「结束条件」时，将「路径」记入结果集
