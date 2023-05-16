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
            'book_no': [1, 3, 5, 7, 11, 23, 35, 55, 56, 61],
            'query': 5
        },
        'output': 2
        },
    {
        'name': 'query found in the first element',
        'input': {
            'book_no': [1, 3, 5, 7, 11, 23, 35, 55, 56, 61],
            'query': 1
        },
        'output': 0
    },
    {
        'name': 'query found in the last element',
        'input': {
            'book_no': [1, 3, 5, 7, 11, 23, 35, 55, 56, 61],
            'query': 61
        },
        'output': 9
    },
    {
        'name': 'query not found in list book',
        'input': {
            'book_no': [1, 3, 5, 7, 11, 23, 35, 55, 56, 61],
            'query': 50
        },
        'output': -1
    }
]
                
dsa = DSA('algorithm', 'binary_search')
passed_cases = 0
failed_cases = 0
total_tests = len(tests)

for index, test in enumerate(tests):
    result = dsa.binary_search(tests[index]['input']['book_no'], tests[index]['input']['query'])
    print('Input:')
    print(tests[index]['input'])
    print()

    print('Expected Output:')
    print(tests[index]['output'])
    print()

    print('Actual Output:')
    print(result)
    print()

    print('Test Result:')
    if tests[index]['output'] == result:
        print('PASSED')
        passed_cases += 1
    else:
        print('FAILED')
        failed_cases += 1

    print()

print(passed_cases, '/', total_tests)