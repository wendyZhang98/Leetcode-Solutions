### Link
# https://leetcode-cn.com/problems/remove-linked-list-elements/solution/chi-xiao-dou-python-di-gui-die-dai-shuan-fayy/


### Description
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。
# 传入函数的唯一参数为 要被删除的节点

# 输入：head = [4,5,1,9], node = 5
# 输出：[4,1,9]
# 解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


### Solution
# 将 node.next 节点的值赋给 node
# 然后将 node.next 指向 node.next 的下一个节点

# Definition for singly-linked list.
class Node(object):
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next


### 迭代法
def deleteNode(head, delete_node_val):
    """
    :param LinkedList
    :param Int
    :return: do not return anything, modify node in-place instead.
    """
    tmp = Node()
    tmp.next = head
    node = tmp
    # tmp：便于返回最终结果
    # node节点向后遍历
    while node and node.next: # 删除 非末尾节点
        if node.value == delete_node_val:
            node.value = node.next.value
            node.next = node.next.next
        else:
            node = node.next
    return tmp.next

### 递归法
def removeElements(head, delete_node_val):
    """
    :param LinkedList
    :param Int
    :return: do not return anything, modify node in-place instead.
    """
    if head is None:
        return head
    head.next = removeElements(head.next, delete_node_val)
    if head.val == delete_node_val:
        next_node = head.next
    else:
        next_node = head
    return next_node

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
root = deleteNode(head=link, delete_node_val=4)
while root:
    print(root.value)
    root = root.next