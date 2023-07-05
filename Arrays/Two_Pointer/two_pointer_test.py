from two_pointer import is_palindrome

tests = [
    {
        'test_case': 'Input is palindrome',
        'query': 'madam',
        'output': True
    },
    {
        'test_case': 'Input is not palindrome',
        'query': 'Joshua',
        'output': True
    }
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f'Test Case {i + 1}:', test['test_case'])
    print(f'Expected Output:', test['output'])
    result = is_palindrome(test['query'])
    print(f'Actual Output:', result)
    
    if result == test['output']:
        print("--- PASSED ---")
        passed_cases += 1
        print()
    else:
        print("--- FAILED ---")
        failed_cases += 1
        print()

print('*' * 100, '\n')
print(f'Result: {passed_cases}/{total_cases} \n')