### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0055.Jump%20Game/README.md


### Description:
# 给定一个非负整数数组 nums，你最初位于数组的第一个下标
# 数组中的每个元素代表你在该位置可以跳跃的最大长度
# 判断你是否能够到达最后一个下标


### Example:
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1
# 然后再从下标 1 跳 3 步到达最后一个下标

# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置
# 但该下标的最大跳跃长度是 0，所以永远不可能到达最后一个下标


### 贪心算法
# 思路：尽可能到达最远位置；如果能到达某个位置，那么一定能到达此位置之前的所有位置
# 方法：初始化最远位置为0；遍历数组，如果当前位置能到达，并且当前位置+jump>=最远位置，更新最远位置


class Solution:
    def canJump(self, nums) :
        max_i = 0                               # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):         # i为当前位置，jump是当前位置的跳数
            if max_i >= i and i+jump > max_i:   # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump                  # 更新最远能到达位置
        return max_i >= i


print(Solution().canJump(nums=[2, 3, 1, 3, 4]))
