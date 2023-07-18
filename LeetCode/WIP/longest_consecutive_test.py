from longest_consecutive import longest_consecutive

tests = [
    {"query": [100, 4, 200, 1, 3, 2], "output": 4},
    {"query": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], "output": 9},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = longest_consecutive(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
