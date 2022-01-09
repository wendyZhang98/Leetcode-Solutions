### Link：
# https:https://www.runoob.com/python3/python-merge-sort.html



### 归并排序：
# 归并排序（MERGE-SORT）是建立在归并操作上的一种有效的排序算法
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用
# 归并排序适用于子序列有序的数据排序

# 归并排序是分治法的典型应用
# 分治法（Divide-and-Conquer）：
# 将原问题划分成 n 个规模较小而结构与原问题相似的子问题；
# 递归地解决这些问题，然后再合并其结果，就得到原问题的解。
# 从上图看分解后的数列很像一个二叉树。

# 归并排序采用分而治之的原理：
# - 将一个序列从中间位置分成两个序列；
# - 在将这两个子序列按照第一步继续二分下去；
# - 直到所有子序列的长度都为1，也就是不可以再二分截止。这时候再两两合并成一个有序序列即可。



### Solution:
def merge_sort(arr):
  if len(arr) == 1:
    return arr
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]
  return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
  result = []
  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  result += left
  result += right
  return result

merge_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22])
