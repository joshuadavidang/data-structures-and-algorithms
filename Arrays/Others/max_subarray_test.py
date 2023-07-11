from max_subarray import max_subarray

tests = [
    {"test_case": "Empty array []", "query": [], "output": []},
    {"test_case": "One element in array [5]", "query": [5], "output": 5},
    {
        "test_case": "Largest maximum sum of [-2,1,-3,4,-1,2,1,-5,4]",
        "query": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        "output": 6,
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}:", test["test_case"])
    print(f"Expected Output:", test["output"])
    result = max_subarray(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
