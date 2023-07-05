from max_prod_subarray import max_product

tests = [
    {
        'test_case': 'Empty array []',
        'query': [],
        'output': 0
    },
    {
        'test_case': 'One element in array [5]',
        'query': [5],
        'output': 5
    },
    {
        'test_case': 'Largest maximum product subarray [[2,3,-2,4]',
        'query': [2,3,-2,4],
        'output': 6
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f'Test Case {i + 1}:', test['test_case'])
    print(f'Expected Output:', test['output'])
    result = max_product(test['query'])
    print(f'Actual Output:', result)
    
    if result == test['output']:
        print("------ PASSED ------")
        passed_cases += 1
        print()
    else:
        print("------ FAILED ------")
        failed_cases += 1
        print()

print('*' * 100, '\n')
print(f'Result: {passed_cases}/{total_cases} \n')