from reverse_array import reverse_array

tests = [
    {
        "test_case": "Reverse array",
        "query": [10, 20, 30, 40, 50],
        "output": [50, 40, 30, 20, 10],
    },
    {"test_case": "Reverse array with 0 element", "query": [], "output": []},
    {"test_case": "Reverse array with 1 element", "query": [10], "output": [10]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}:", test["test_case"])
    print(f"Expected Output:", test["output"])
    result = reverse_array(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("--- PASSED --- \n")
        passed_cases += 1
    else:
        print("--- FAILED --- \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
