### Difficult Level: Medium
### https://practice.geeksforgeeks.org/problems/quick-sort/1
### https://en.wikipedia.org/wiki/Quicksort
### https://zhuanlan.zhihu.com/p/63227573



### 复杂度分析: 
# https://harttle.land/2015/09/27/quick-sort.html




### 快速排序介绍：
# 快速排序的核心思想是分治：
# 选择数组中某个数作为基数，
# 通过一趟排序将要排序的数据分割成独立的两部分，
# 其中一部分的所有数都比基数小，
# 另外一部分的所有数都都比基数大，
# 然后再按此方法对这两部分数据分别进行快速排序，循环递归，最终使整个数组变成有序。
 
    
   
  
### 算法步骤:
# 从数列中挑出一个元素，称为 "基准"（pivot）;
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）
# 在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；




### Description:
# Quick Sort is a Divide and Conquer algorithm
# It picks an element as pivot and partitions the given array around the picked pivot
# Given an array arr[], its starting position low and its ending position high.
# Implement the partition() and quickSort() functions to sort the array




### Solution:
### Link: https://blog.csdn.net/liangkaiping0525/article/details/82558188
def quick_sort(lst, i, j):
    if i >= j:
        return lst
    
    pivot = lst[i]
    low = i
    high = j
    
    while i < j:
        while i < j and lst[j] >= pivot:
            j -= 1
        lst[i] = lst[j]
        while i < j and lst[i] <= pivot:
            i += 1
        lst[j] = lst[i]
       
    lst[j] = pivot
    quick_sort(lst, low, i-1)
    quick_sort(lst, i+1, high)
    return lst


if __name__=="__main__":
    lst = [30,24,5,58,18,36,12,42,39]
    print(f'Before quick sort: {lst}')

    lst = quick_sort(lst, 0, len(lst)-1)
    print(f'After quick sort: {lst}')
