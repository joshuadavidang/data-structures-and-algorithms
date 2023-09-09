from mergeSort import sortArray

tests = [
    {"query": [5, 4, 3, 2, 1], "output": [1, 2, 3, 4, 5]},
    {"query": [5, 1, 1, 2, 0, 0], "output": [0, 0, 1, 1, 2, 5]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = sortArray(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
