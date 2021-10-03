### Link:
# https://stackoverflow.com/questions/18262306/quicksort-with-python


### 快速排序(Quick Sort)是对冒泡排序的一种改进。
# 其的基本思想:
# 选一基准元素，依次将剩余元素中小于该基准元素的值放置其左侧，大于等于该基准元素的值放置其右侧；
# 然后，取基准元素的前半部分和后半部分分别进行同样的处理；
# 以此类推，直至各子序列剩余一个元素时，即排序完成（类比二叉树的思想)

### 快速排序步骤
# 首先设定一个分界值(pivot)，通过该分界值将数组分成左右两部分。
# 将大于或等于分界值的数据集中到数组右边，小于分界值的数据集中到数组的左边。
# 此时，左边部分中各元素都小于或等于分界值，而右边部分中各元素都大于或等于分界值,这个称为分区（partition）操作。
# 然后，左边和右边的数据可以独立排序。
# 对于左侧的数组数据，又可以取一个分界值，将该部分数据分成左右两部分，同样在左边放置较小值，右边放置较大值。
# 右侧的数组数据也可以做类似处理。
# 重复上述过程，通过递归（recursive）将左侧部分排好序后，再递归排好右侧部分的顺序。
# 当左、右两个部分各数据排序完成后，整个数组的排序也就完成了。


def quicksort(array):
    """Sort the array by using quicksort."""
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less) + equal + quicksort(greater) # recursion
    # You need to handle the part at the end of the recursion
    # when you only have one element in your array, just return the array
    else:
        return array

print(f'After Quick Sort: {quicksort([12, 11, 8, 15, 3, 2])}')

