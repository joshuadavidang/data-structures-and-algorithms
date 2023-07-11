from max_profit import max_profit

tests = [
    {"test_case": "Array less than 2 elements", "query": [], "output": 0},
    {
        "test_case": "Array more than 2 elements",
        "query": [7, 1, 5, 3, 6, 4],
        "output": 5,
    },
    {"test_case": "Array more than 2 elements", "query": [7, 6, 4, 3, 1], "output": 0},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}:", test["test_case"])
    print(f"Expected Output:", test["output"])
    result = max_profit(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
