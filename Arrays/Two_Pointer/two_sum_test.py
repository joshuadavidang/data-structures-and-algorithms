from two_sum import two_sum

tests = [
    {
        "test_case": "Case 1",
        "query": [[2, 7, 11, 15], 9],
        "output": [0, 1],
    },
    {
        "test_case": "Case 2",
        "query": [[3, 2, 4], 6],
        "output": [1, 2],
    },
    {
        "test_case": "Case 3",
        "query": [[3, 3], 6],
        "output": [0, 1],
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}:", test["test_case"])
    print(f"Expected Output:", test["output"])
    result = two_sum(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------")
        passed_cases += 1
        print()
    else:
        print("------ FAILED ------")
        failed_cases += 1
        print()

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
