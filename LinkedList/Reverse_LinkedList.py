### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0206.Reverse%20Linked%20List/README.md


### Description:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


### Method1：迭代
# 链表的反转引入一个cur_node变量，表示当前节点；
# 同时需要引入一个变量new_link表示反转后的新链表；
# while循环内还需中间变量tmp存放当前节点的后继节点，防止原链表数据丢失。


class Node(object):
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next


class Solution:
    def reverseList(head):
        new_link, cur_node = None, head
        # new reversed linked_lst, current node
        while cur_node:
            tmp = cur_node.next # save current_node.next as tmp
            cur_node.next = new_link # current_node point to the new reversed linked_lst
            new_link = cur_node # update the new reversed linked_lst as current_node
            cur_node = tmp # update the current_node (move along the old linked_lst)
        return new_link


### Method2：递归【❌】
# 递归实现与while实现不同在于递归首先找到新链表的头部节点，然后递归栈返回，层层反转
# 递归的方法非常巧，它利用递归走到链表的末端。然后再更新每一个node的next值, 实现链表的反转
# 而newhead的值没有发生改变，为该链表的最后一个结点。所以，反转后，我们可以得到新链表的head

def reverseList2(head):
    if head.next == None:
        return head
    new_head = reverseList2(head.next)
    head.next.next = head
    head.next = None

    return new_head


link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

print('Method 1: Iteration')
root = Solution.reverseList(head=link)
while root:
    print(root.value)
    root = root.next

root2 = reverseList2(head=link)
print('Method2: Recursion')
while root2:
    print(root2.value)
    root2 = root2.next