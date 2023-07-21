from maximum_subarray import maximum_subarray

tests = [
    {"query": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "output": 6},
    {"query": [1], "output": 1},
    {"query": [5, 4, -1, 7, 8], "output": 23},
    {"query": [-3, -4, 5, -1, 2, -4, 6, -1], "output": 8},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = maximum_subarray(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
