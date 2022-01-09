### Link:
# https://www.runoob.com/python3/python-insertion-sort.html
# https://www.youtube.com/watch?v=uvxHAH3Wq2I


### 插入排序（英语：Insertion Sort）是一种简单直观的排序算法
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入


### 算法步骤：
# 从第二个元素（第一个需要被排序的元素）开始，从后向前扫描之前的元素序列
# 如果当前扫描的元素大于新元素，将扫描元素移动到下一位
# 重复步骤2，直到找到一个小于等于新元素的位置
# 将新元素插入到该位置
# 对于之后的元素重复步骤1-4


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
print(f"After InsertionSort: {insertionSort(arr)}")
