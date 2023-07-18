from find_min import find_min

tests = [
    {"query": [3, 4, 5, 1, 2], "output": 1},
    {"query": [4, 5, 6, 7, 0, 1, 2], "output": 0},
    {"query": [1, 2, 3, 4, 5], "output": 1},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = find_min(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
