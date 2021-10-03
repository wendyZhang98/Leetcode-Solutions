### Link:
# https://github.com/doocs/leetcode/blob/main/lcof/%E9%9D%A2%E8%AF%95%E9%A2%9806.%20%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8/README.md


### Description:
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）


# Definition for singly-linked list.
class Node(object):
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next

def reversePrint(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst[::-1]


link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
reverse_lst = reversePrint(head=link)
print(f'The reverse list is: {reverse_lst}')