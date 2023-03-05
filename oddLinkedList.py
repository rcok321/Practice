class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def regeneratedList(head):

    odd_head = ListNode()
    even_head = ListNode()

    odd_node = odd_head
    even_node = even_head

    index = 1
    cur_node = head

    while cur_node:
        if index % 2 == 1:  # 如果當前節點的位置是奇數
            odd_node.next = cur_node  # 將當前節點添加到奇數 Linked List
            odd_node = odd_node.next
        else:  # 如果當前節點的位置是偶數
            even_node.next = cur_node  # 將當前節點添加到偶數 Linked List
            even_node = even_node.next

        # 移動到下一個節點
        cur_node = cur_node.next
        index += 1

    if even_head.next:
    	odd_node.next = regeneratedList(even_head.next)
    else:
    	odd_head.next = None

    # 返回奇偶 Linked List 的頭節點
    return odd_head.next

    
if __name__ == "__main__":
	list1 = ListNode(1)
	list1.next = ListNode(2)
	list1.next.next = ListNode(3)
	list1.next.next.next = ListNode(4)
	list1.next.next.next.next = ListNode(5)
	list1.next.next.next.next.next = ListNode(6)
	list1.next.next.next.next.next.next = ListNode(7)
	list2 = regeneratedList(list1)

	while list2:
		print(list2.data, end=" ")
		list2 = list2.next