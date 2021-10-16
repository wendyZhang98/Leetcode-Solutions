### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0045.Jump%20Game%20II/README.md


### Description:
# 给定一个非负整数数组，你最初位于数组的第一个位置
# 数组中的每个元素代表你在该位置可以跳跃的最大长度
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置


### Example:
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。


# 假设你总是可以到达数组的最后一个位置。



### Solution:
# 具体的实现中，我们维护当前能够到达的最大下标位置，记为边界。
# 我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。

# 在遍历数组时，我们不访问最后一个元素，
# 这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，
# 否则就无法跳到最后一个位置了。
# 如果访问最后一个元素，在边界正好为最后一个位置的情况下，
# 我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。

# https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
class Solution:
    def jump(self, nums):
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

# print(Solution().jump(nums=[2, 3, 1, 3, 4]))
