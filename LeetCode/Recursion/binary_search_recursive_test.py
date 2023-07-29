from binary_search_recursive import binarySearch

tests = [
    {"query": [[-1, 0, 3, 5, 9, 12], 9], "output": 4},
    {"query": [[-1, 0, 3, 5, 9, 12], 2], "output": -1},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = binarySearch(
        test["query"][0], test["query"][1], 0, len(test["query"][0]) - 1
    )
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
