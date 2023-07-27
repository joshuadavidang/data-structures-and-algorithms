from sort_colors import sortColors

tests = [
    {"query": [2, 0, 2, 1, 1, 0], "output": [0, 0, 1, 1, 2, 2]},
    {"query": [2, 0, 1], "output": [0, 1, 2]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = sortColors(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
