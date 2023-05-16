class DSA:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def binary_search(self, books, target):
        left, right = 0, len(books) - 1
        while left <= right:
            mid = (left + right) // 2
            if books[mid] > target:
                right = mid - 1          
            elif books[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
    
tests = [
    {
        'name': 'query found in list book',
        'input': {
            'book_no': [1, 3, 5, 7, 11, 23, 35, 55, 56, 61, 33],
            'query': 5
        },
        'output': 2
        },
    {
        'name': 'query not found in list book',
        'input': {
            'book_no': [1, 3, 5, 7, 11, 23, 35, 55, 56, 61, 33],
            'query': 50
        },
        'output': -1
    }
]
                
dsa = DSA("algorithm", "binary_search")
for i in range(len(tests)):
    result = dsa.binary_search(tests[i]['input']['book_no'], tests[i]['input']['query'])
    print("Input:")
    print(tests[i]['input'])
    print()

    print("Expected Output:")
    print(tests[i]['output'])
    print()

    print("Actual Output:")
    print(result)
    print()

    print("Test Result:")
    if tests[i]['output'] == result:
        print("PASSED")
    else:
        print("FAILED")

    print()