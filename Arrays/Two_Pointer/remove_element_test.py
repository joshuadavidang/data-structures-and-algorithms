from remove_element import remove_element

tests = [
    {
        "test_case": "Remove element with the value 3",
        "query": [3, 2, 2, 3],
        "param": 3,
        "output": 2,
    },
    {
        "test_case": "Remove element with the value 2",
        "query": [0, 1, 2, 2, 3, 0, 4, 2],
        "param": 2,
        "output": 5,
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}:", test["test_case"])
    print(f"Expected Output:", test["output"])
    result = remove_element(test["query"], test["param"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("--- PASSED --- \n")
        passed_cases += 1
    else:
        print("--- FAILED --- \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
