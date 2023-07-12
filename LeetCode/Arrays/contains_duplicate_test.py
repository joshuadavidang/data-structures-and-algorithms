from contains_duplicate import contains_duplicate

tests = [
    {"query": [1, 2, 3, 1], "output": True},
    {"query": [1, 2, 3, 4], "output": False},
    {"query": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], "output": True},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = contains_duplicate(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
