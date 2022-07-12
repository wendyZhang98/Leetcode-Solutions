### Descriptions:
- https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0016.3Sum%20Closest/README.md
- https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-by-leetcode-solution/
- 给定一个包括 n 个整数的数组 nums 和 一个目标值 target
- 找出 nums 中的三个整数，使得它们的和与 target 最接近
- 返回这三个数的和, 假定每组输入只存在唯一答案


### Examples:
- Input: nums = [-1, 2, 1, -4], target = 1
- Output: 2
- 与 target 最接近的和是 2(-1 + 2 + 1 = 2)


### Solutions:
- 枚举 a， 它在数组中的位置为i
- 为了防止重复枚举，在 i+1，n 范围内枚举 b 和 c
- 对数组进行（升序）排序，借助双指针优化排序
- 用 pb 和 pc 分别表示指向 b 和 c 的指针
- 初始时刻，pb 指向位置i+1，即左边界；pc 指向位置n-1，即右边界
- 在每一步枚举的过程中计算 a+b+c 来更新答案
- 如果 a+b+c >= target，那么将 pc 向左移动一个位置
- 如果 a+b+c < target，那么将 pb 向右移动一个位置


```
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        best = 10**7
        
        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best
```
