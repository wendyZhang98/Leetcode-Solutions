### Link：
# https:https://www.runoob.com/python3/python-merge-sort.html


### 归并排序（英语：Merge sort)是创建在归并操作上的一种有效的排序算法
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用


### 分治法（Divide-and-Conquer):
# 将原问题划分成 n 个规模较小而结构与原问题相似的子问题
# 递归地解决这些问题，然后再合并其结果，就得到原问题的解

### 图片：https://www.cnblogs.com/pythonbao/p/10800699.html
def mergesort(seq):
    # 1st: [5 3 0 6 1 4]
    # 2nd: [5 3 0]

    if len(seq) <= 1:
        return seq

    ## divide the sequence into smaller ones
    mid = len(seq) // 2
    # 1st: 3
    # 2nd: 1

    ## separately address the left/right sequence
    left = mergesort(seq[:mid])
    # 1st: mergesort([5 3 0])
    # 2nd: mergesort([5])
    # 3nd: mergesort([6])

    right = mergesort(seq[mid:])
    # 1st: mergesort([6 1 4])
    # 2nd: mergesort([3 0])
    # 3nd: mergesort([1 4])

    ## merge the ranked list
    return merge(left, right)
    # merge(mergesort([5 3 0]), mergesort([6 1 4]))
    # merge(merge(mergesort([5]), mergesort([3 0])), merge(mergesort([6]), mergesort([1 4])))
    # merge(merge(mergesort([5]), merge(mergesort([3]), mergesort([0]))),
    #       merge(mergesort([6]), merge(mergesort([1]), mergesort([4]))))

def merge(left, right):
    result = []
    i = 0
    j = 0
    # compare elements in left/right sequence
    # put the smaller element into result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

seq = [5, 3, 0, 6, 1, 4]
result = mergesort(seq)
print(f'After MergeSort: {result}')