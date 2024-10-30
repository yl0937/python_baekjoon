from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        head.next = list1
        prev_li = head
        while list1:
            print(list1.val)
            list1 = prev_li.next
        # list1 = sorted(list1 + list2)
        # head = ListNode(list1[0])
        # curr_node = head
        # new_node = ListNode(list1[1])
        # curr_node.next = new_node
        # curr_node = curr_node.next
        # for i in range(2,len(list1)):
        #     curr_node.next = ListNode(list1[i])
        #     curr_node=curr_node.next
        #
        #
        # node = head
        # while node:
        #     print(node.val)
        #     node = node.next


s = Solution()
print(s.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))