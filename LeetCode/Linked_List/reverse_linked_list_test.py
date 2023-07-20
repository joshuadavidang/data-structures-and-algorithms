from reverse_linked_list import (
    create_linked_list,
    reverseList,
    display_result,
)

tests = [
    {"query": [1, 2, 3, 4, 5], "output": [5, 4, 3, 2, 1]},
    {"query": [1, 2], "output": [2, 1]},
    {"query": [], "output": []},
]

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    head = create_linked_list(test["query"])
    print("Original Linked List:")
    display_result(head)
    head = reverseList(head)
    print("Reversed Linked List:")
    display_result(head)
    print("*" * 100, "\n")
