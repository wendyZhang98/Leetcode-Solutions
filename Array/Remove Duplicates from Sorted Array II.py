### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0080.Remove%20Duplicates%20from%20Sorted%20Array%20II/README.md


### Description:
# 给你一个有序数组 nums ，请你原地删除重复出现的元素，
# 使每个元素最多出现两次 ，返回删除后数组的新长度。

# 不要使用额外的数组空间，你必须在原地修改输入数组
# 并在使用 O(1) 额外空间的条件下完成。

# 为什么返回数值是整数，但输出的答案是数组呢？
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。


### Example:
# 示例1：
# 输入：nums = [1, 1, 1, 2, 2, 3]
# 输出：5, nums = [1, 1, 2, 2, 3]
# 解释：函数应返回新长度
# length = 5, 并且原数组的前五个元素被修改为
# 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

# 示例2：
# 输入：nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# 输出：7, nums = [0, 0, 1, 1, 2, 3, 3]
# 解释：函数应返回新长度
# length = 7, 并且原数组的前五个元素被修改为
# 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。



### Solution:
# 从数组下标 1 开始遍历数组。
# 用计数器 cnt 记录当前数字重复出现的次数，
# cnt 的最小计数为 0；
# 用 cur 记录新数组下个待覆盖的元素位置。
# 遍历时，若当前元素 nums[i] 与上个元素 nums[i-1] 相同，
# 则计数器 +1，否则计数器重置为 0。
# 如果计数器小于 2，说明当前元素 nums[i] 可以添加到新数组中，即：nums[cur] = nums[i]，同时 cur++。
# 遍历结果，返回 cur 值即可



###
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        cnt, cur = 0, 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                cnt = 0
            if cnt < 2:
                nums[cur] = nums[i]
                cur += 1
        return cur