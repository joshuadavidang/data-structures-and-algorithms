from prod_except_self import productExceptSelf

tests = [
    {"query": [1, 2, 3, 4], "output": [24, 12, 8, 6]},
    {"query": [-1, 1, 0, -3, 3], "output": [0, 0, 9, 0, 0]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = productExceptSelf(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
