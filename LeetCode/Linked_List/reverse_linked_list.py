class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def reverseList(head):
    prev, current = None, head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def display_result(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None \n")
